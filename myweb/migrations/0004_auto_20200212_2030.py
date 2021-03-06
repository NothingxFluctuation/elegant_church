# Generated by Django 3.0.1 on 2020-02-12 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20200212_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.IntegerField(blank=True, null=True)),
                ('church_name', models.TextField(blank=True, null=True)),
                ('firstname', models.TextField(blank=True, null=True)),
                ('lastname', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('alternative_phone', models.TextField(blank=True, null=True)),
                ('web', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('license_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='songrequest',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_song_requests', to='myweb.ChurchInformation'),
        ),
        migrations.DeleteModel(
            name='ChurchInfo',
        ),
    ]
