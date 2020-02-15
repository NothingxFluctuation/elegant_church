from django.contrib import admin
from .models import (ExtractAcctSubmit, ExtractAooRef, ExtractArSubmit, ExtractCharity,
                     ExtractClass, ExtractClassRef, ExtractFinancial, ExtractMainCharity,
                     ExtractName, ExtractTrustee, MainTable, AllInformation, MainCharityMerger)


@admin.register(ExtractAcctSubmit)
class ExtractAcctSubmitAdmin(admin.ModelAdmin):
    list_display = ("regno", "submit_date", "arno", "fyend")
    search_fields = ("regno", "submit_date", "arno", "fyend")


@admin.register(ExtractAooRef)
class ExtractAooRefAdmin(admin.ModelAdmin):
    list_display = ("aootype", "aookey", "aoosort", "aooname", "welsh",
                    "master")

    search_fields = ("aootype", "aookey", "aoosort", "aooname", "welsh",
                    "master")

@admin.register(ExtractArSubmit)
class ExtractArSubmitAdmin(admin.ModelAdmin):
    list_display = ("regno", "arno", "submit_date")
    search_fields = ("regno", "arno", "submit_date")




@admin.register(ExtractCharity)
class ExtractCharityAdmin(admin.ModelAdmin):
    list_display = ("regno", "subno", "name", "orgtype", "gd", "aob", "aob_defined", "nhs",
                    "ha_no", "corr", "add1", "add2", "add3", "add4", "add5", "postcode",
                    "phone", "fax")

    search_fields = ("regno", "subno", "name", "orgtype", "gd", "aob", "aob_defined", "nhs",
                    "ha_no", "corr", "add1", "add2", "add3", "add4", "add5", "postcode",
                    "phone", "fax")

@admin.register(ExtractClass)
class ExtractClassAdmin(admin.ModelAdmin):
    list_display = ("regno", "class_field")


@admin.register(ExtractClassRef)
class ExtractClassRefAdmin(admin.ModelAdmin):
    list_display = ("classno", "classtext")
    search_fields = ("classno", "classtext")


@admin.register(ExtractFinancial)
class ExtractFinancialAdmin(admin.ModelAdmin):
    list_display = ("regno", "fystart", "fyend", "income", "expend")
    search_fields = ("regno", "fystart", "fyend", "income", "expend")


@admin.register(ExtractMainCharity)
class ExtractMainCharityAdmin(admin.ModelAdmin):
    list_display = ("regno", "coyno", "fyend", "trustees", "welsh", "incomedate",
                    "income", "grouptype", "email", "web")

    search_fields = ("regno", "coyno", "fyend", "trustees", "welsh", "incomedate",
                    "income", "grouptype", "email", "web")


@admin.register(ExtractName)
class ExtractNameAdmin(admin.ModelAdmin):
    list_display = ("regno", "subno", "nameno", "name")
    search_fields = ("regno", "subno", "nameno", "name")


@admin.register(ExtractTrustee)
class ExtractTrusteeAdmin(admin.ModelAdmin):
    list_display = ("regno", "trustee")
    search_fields = ("regno", "trustee")


@admin.register(MainTable)
class MainTableAdmin(admin.ModelAdmin):
    list_display = ('index', 'regno', 'subno', 'name', 'orgtype', 'gd',
                    'aob', 'aob_defined', 'nhs', 'ha_no', 'postcode', 'phone', 'fax',
                    'fyend', 'fystart', 'income')

    search_fields = ('index', 'regno', 'subno', 'name', 'orgtype', 'gd', 'aob',
                     'aob_defined', 'nhs', 'ha_no', 'postcode',
                     'phone', 'fax', 'fyend', 'fystart', 'income')


@admin.register(AllInformation)
class AllInformationAdmin(admin.ModelAdmin):
    list_display = ('index', 'regno', 'subno', 'name', 'orgtype', 'gd', 'aob', 'aob_defined', 'nhs',
                    'ha_no', 'corr', 'add1', 'add2', 'add3', 'add4', 'add5', 'postcode', 'phone', 'fax',
                    'income', 'expend','financial_year_start', 'financial_year_end', 'email', 'incomedate', 'web')

    search_fields = ('index', 'regno', 'subno', 'name', 'orgtype', 'gd', 'aob', 'aob_defined', 'nhs',
                   'ha_no', 'corr', 'add1', 'add2', 'add3', 'add4', 'add5', 'postcode', 'phone', 'fax',
                   'income', 'expend', 'financial_year_start', 'financial_year_end', 'email', 'incomedate', 'web')


@admin.register(MainCharityMerger)
class MainCharityMergerAdmin(admin.ModelAdmin):
    list_display = ('index', 'regno', 'name', 'gd', 'aob',
                    'ha_no', 'corr', 'add1', 'add2', 'add3', 'add4', 'add5', 'postcode', 'phone', 'fax', 'web', 'email')

    search_fields = ('index', 'regno', 'name', 'gd', 'aob',
                     'ha_no', 'corr', 'add1', 'add2', 'add3', 'add4', 'add5', 'postcode', 'phone', 'fax', 'web', 'email')
