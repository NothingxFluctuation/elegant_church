from django.shortcuts import render
from extract.models import MainCharityMerger, ExtractFinancial
from django.http import HttpResponse
from .forms import RegistrationForm, SongRequestForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import ChurchInformation, SongRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def log_me_out(request):
    auth_logout(request)
    return redirect('home')

def start(request):
    return render(request, 'start.html')

def home(request):
    if request.user.is_authenticated:
        church = ChurchInformation.objects.get(regno=1172410)
        return render(request,'main.html',{'church':church})
    return render(request,'index2.html')




def get_regno(request):
    rg = request.GET.get('rgno')
    mcg = MainCharityMerger.objects.filter(regno=rg)
    if len(mcg) > 0:
        mcg_obj = MainCharityMerger.objects.get(regno=rg)
        data = {'regno':mcg_obj.regno, 'churchname':mcg_obj.name, 'address': mcg_obj.add1, 'phone':mcg_obj.phone, 'web':mcg_obj.web, 'email':mcg_obj.email}
        return render(request,'signup.html',data)
    else:
        return HttpResponse('no church with such registration number found.')

def log_me_in(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    user_f = User.objects.filter(email=email)
    if len(user_f) > 0:
        user = User.objects.get(email=email)
        check = user.check_password(password)
        if check:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'index2.html')
    return render(request, "index2.html")


def get_regnoo(request):
    if request.method =='POST':
        r_form = RegistrationForm(request.POST)
        if r_form.is_valid():
            regno = request.POST['regno']
            ef = ExtractFinancial.objects.filter(regno=regno)
            incm = None
            for e in ef:
                nc = e.income
                if nc != '':
                    incm = nc
                    break
            ef = str(incm)
            if incm == '' or incm == None:
                incm = 0
            if incm < 100000:
                lt = 'A'
                pym = '€100 per Month or €1000 per anum'
            elif incm >= 100000 and incm <= 500000:
                lt = 'B'
                pym = '€275 per Month or €3300 per anum'
            elif incm > 500000 and incm <=1000000:
                lt = 'C'
                pym = '€350 per Month or €4200 per anum'
            elif incm > 1000000 and incm <=10000000:
                lt = 'D'
                pym = '€750 per Month or €9000 per anum'
            else:
                lt = 'E'
                pym = '€1500 per Month or €18000 per anum'
            username = request.POST['name']
            password = request.POST['password']
            email = request.POST['email']
            u = User.objects.create(username=username,email = email)
            u.set_password(password)
            u.save()
            login(request,u)
            r_obj = r_form.save(commit=False)
            r_obj.license_type = lt
            r_obj.save()
            return render(request,'payment.html',{'payment':ef,'pym':pym})
        else:
            
            print(r_form.errors)
            return HttpResponse('no income found')
    rg = request.GET.get('rgno')
    mcg = MainCharityMerger.objects.filter(regno=rg)
    if len(mcg) > 0:
        mcg_obj = MainCharityMerger.objects.get(regno=rg)
        r_form = RegistrationForm(instance = mcg_obj)
        return render(request,'reg_showinfo.html',{'r_form':r_form})
    else:
        return HttpResponse('no church with such registration number found.')


def get_test(request):
    church = ChurchInformation.objects.get(regno=1172410)
    sr = SongRequest.objects.filter(church=church)
    return render(request,'love.html',{'songs':sr})


@csrf_exempt
@login_required
def new_song(request):
    if request.method == 'POST':
        song_form = SongRequestForm(request.POST)
        if song_form.is_valid():
            yt = request.POST['youtube_link']
            it = request.POST['itunes_link']
            spt = request.POST['spotify_link']
            if yt or it or spt:
                song_obj = song_form.save(commit=False)
                usrnm = request.user.username
                usrnm = str(usrnm)
                print(usrnm)
                chrch = ChurchInformation.objects.get(church_name = usrnm)
                song_obj.church = chrch
                song_obj.save()
                return HttpResponse("done")
            else:
                return HttpResponse("no")  
        return HttpResponse("no")      
        
    
    song_form = SongRequestForm()
    return render(request,'new_song.html',{'song_form':song_form})


@login_required
def all_songs(request):
    usrnm = request.user.username
    usrnm = str(usrnm)
    chrch = ChurchInformation.objects.get(name = usrnm)
    songs = chrch.my_song_requests.all()
    return render(request,'all_songs.html',{'songs':songs})



@login_required
def edit_profile(request):
    chrch = ChurchInformation.objects.get(regno=1172410)
    if request.method == 'POST':
        chrch_form = RegistrationForm(instance=chrch, data=request.POST)
        if chrch_form.is_valid():
            chrch_form.save()
            return HttpResponse("done")
        else:
            return HttpResponse("no")
    return render(request,'church_data.html',{'church':church})



import gocardless_pro

@login_required
def Handle_Payment(request):
    client = gocardless_pro.Client(
    access_token= "sandbox_B0pUDWsTgiJ-jK-jo4-M8KUp7xxS0-I_pgnc4-vr", 
    environment='sandbox'
    )
    redirect_flow = client.redirect_flows.create(
    params={
        "description" : "EBENEZER CHURCH Subscription Setup", # This will be shown on the payment pages
        "session_token" : "Jl0--Klnzjdlw30fjallZKo", # Not the access token
        "success_redirect_url" : "https://developer.gocardless.com/example-redirect-uri/",
        # "prefilled_customer": { # Optionally, prefill customer details on the payment page
        #     "given_name": "Tim",
        #     "family_name": "Rogers",
        #     "email": "tim@gocardless.com",
        #     "address_line1": "338-346 Goswell Road",
        #     "city": "London",
        #     "postal_code": "EC1V 7LQ"
        #     }
        }
    )

    # Hold on to this ID - we'll need it when we
    # "confirm" the redirect flow later
    print("ID: {} ".format(redirect_flow.id))
    print("URL: {} ".format(redirect_flow.redirect_url))
    ru = redirect_flow.redirect_url
    return redirect(ru)


def payme(request):
    return render(request,'payme.html')