# Generated by Django 3.0.1 on 2020-02-12 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='churchinfo',
            name='license_type',
        ),
    ]
