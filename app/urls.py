"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import myweb.views as mywebviews
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('',mywebviews.home, name='home'),
    path('start/',mywebviews.start, name='start'),
    path('registration_regno/',mywebviews.get_regno, name='get_regno'),
    path('login/', mywebviews.log_me_in,name='login'),
    path('logout/',mywebviews.log_me_out,name='logout'),
    path('edit_profile/',mywebviews.edit_profile, name='edit_profile'),
    path('payme/',mywebviews.payme, name='payme'),
    path('handle_payment/',mywebviews.Handle_Payment, name='handle_payment'),

    path('new_song/',mywebviews.new_song, name='new_song'),
    path('all_songs/',mywebviews.all_songs, name='all_songs'),
    path('get_test/',mywebviews.get_test,name='get_test'),

    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
