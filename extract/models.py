# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ExtractAcctSubmit(models.Model):
    regno = models.CharField(max_length=24, blank=True, null=True)
    submit_date = models.DateField(blank=True, null=True)
    arno = models.CharField(max_length=14, blank=True, null=True)
    fyend = models.CharField(max_length=14, blank=True, null=True)
    index = models.IntegerField(null=False, primary_key=True)

    class Meta:
        db_table = 'extract_acct_submit'


class ExtractAooRef(models.Model):
    aootype = models.CharField(max_length=10)
    aookey = models.IntegerField()
    aooname = models.CharField(max_length=50)
    aoosort = models.CharField(max_length=50)
    welsh = models.CharField(max_length=10)
    index = models.IntegerField(null=False, primary_key=True)
    master = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'extract_aoo_ref'


class ExtractArSubmit(models.Model):
    regno = models.CharField(max_length=20)
    arno = models.CharField(max_length=8)
    submit_date = models.DateField()
    index = models.IntegerField(null=False, primary_key=True)

    class Meta:
        db_table = 'extract_ar_submit'


class ExtractCharity(models.Model):
    index = models.BigIntegerField(null=False, primary_key=True)
    regno = models.TextField(blank=True, null=True)
    subno = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    orgtype = models.TextField(blank=True, null=True)
    gd = models.TextField(blank=True, null=True)
    aob = models.TextField(blank=True, null=True)
    aob_defined = models.TextField(blank=True, null=True)
    nhs = models.TextField(blank=True, null=True)
    ha_no = models.TextField(blank=True, null=True)
    corr = models.TextField(blank=True, null=True)
    add1 = models.TextField(blank=True, null=True)
    add2 = models.TextField(blank=True, null=True)
    add3 = models.TextField(blank=True, null=True)
    add4 = models.TextField(blank=True, null=True)
    add5 = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'extract_charity'


class ExtractClass(models.Model):
    index = models.BigIntegerField(null=False, primary_key=True)
    regno = models.FloatField(blank=True, null=True)
    class_field = models.FloatField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'extract_class'


class ExtractClassRef(models.Model):
    index = models.BigIntegerField(null=False, primary_key=True)
    classno = models.FloatField(blank=True, null=True)
    classtext = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'extract_class_ref'


class ExtractFinancial(models.Model):
    index = models.BigIntegerField(null=False, primary_key=True)
    regno = models.FloatField(blank=True, null=True)
    fystart = models.DateTimeField(blank=True, null=True)
    fyend = models.DateTimeField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    expend = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'extract_financial'


class ExtractMainCharity(models.Model):
    index = models.BigIntegerField(null=False, primary_key=True)
    regno = models.FloatField(blank=True, null=True)
    coyno = models.TextField(blank=True, null=True)
    trustees = models.TextField(blank=True, null=True)
    fyend = models.FloatField(blank=True, null=True)
    welsh = models.TextField(blank=True, null=True)
    incomedate = models.TextField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    grouptype = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    web = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'extract_main_charity'


class ExtractName(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    regno = models.FloatField(blank=True, null=True)
    subno = models.FloatField(blank=True, null=True)
    nameno = models.FloatField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'extract_name'


class ExtractTrustee(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    regno = models.FloatField(blank=True, null=True)
    trustee = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'extract_trustee'




class ExtractTrustee(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    regno = models.FloatField(blank=True, null=True)
    trustee = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extract_trustee'


class MainTable(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    regno = models.IntegerField(blank=True, null=True)
    subno = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    orgtype = models.TextField(blank=True, null=True)
    gd = models.TextField(blank=True, null=True)
    aob = models.TextField(blank=True, null=True)
    aob_defined = models.TextField(blank=True, null=True)
    nhs = models.TextField(blank=True, null=True)
    ha_no = models.TextField(blank=True, null=True)
    corr = models.TextField(blank=True, null=True)
    add1 = models.TextField(blank=True, null=True)
    add2 = models.TextField(blank=True, null=True)
    add3 = models.TextField(blank=True, null=True)
    add4 = models.TextField(blank=True, null=True)
    add5 = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.FloatField(blank=True, null=True)
    fyend = models.TextField(blank=True, null=True)
    fystart = models.TextField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)

    class Meta:

        db_table = 'main_table'


class AllInformation(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    regno = models.IntegerField(blank=True, null=True)
    subno = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    orgtype = models.TextField(blank=True, null=True)
    gd = models.TextField(blank=True, null=True)
    aob = models.TextField(blank=True, null=True)
    aob_defined = models.TextField(blank=True, null=True)
    nhs = models.TextField(blank=True, null=True)
    ha_no = models.TextField(blank=True, null=True)
    corr = models.TextField(blank=True, null=True)
    add1 = models.TextField(blank=True, null=True)
    add2 = models.TextField(blank=True, null=True)
    add3 = models.TextField(blank=True, null=True)
    add4 = models.TextField(blank=True, null=True)
    add5 = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.FloatField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    expend = models.FloatField(blank=True, null=True)
    financial_year_start = models.TextField(blank=True, null=True)
    financial_year_end = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    incomedate = models.TextField(blank=True, null=True)
    web = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'all_information'


class MainCharityMerger(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    regno = models.IntegerField(blank=True, null=True)
    subno = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    orgtype = models.TextField(blank=True, null=True)
    gd = models.TextField(blank=True, null=True)
    aob = models.TextField(blank=True, null=True)
    aob_defined = models.TextField(blank=True, null=True)
    nhs = models.TextField(blank=True, null=True)
    ha_no = models.TextField(blank=True, null=True)
    corr = models.TextField(blank=True, null=True)
    add1 = models.TextField(blank=True, null=True)
    add2 = models.TextField(blank=True, null=True)
    add3 = models.TextField(blank=True, null=True)
    add4 = models.TextField(blank=True, null=True)
    add5 = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.FloatField(blank=True, null=True)
    web = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'main_charity_merger'
