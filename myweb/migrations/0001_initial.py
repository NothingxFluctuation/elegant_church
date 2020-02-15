# Generated by Django 3.0.1 on 2020-02-12 11:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchInfo',
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
            options={
                'db_table': 'church_info',
            },
        ),
        migrations.CreateModel(
            name='SongRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_for', models.CharField(max_length=50)),
                ('song_artist', models.CharField(max_length=150)),
                ('song_title', models.CharField(max_length=1000)),
                ('youtube_link', models.CharField(max_length=1000)),
                ('itunes_link', models.CharField(max_length=1000)),
                ('spotify_link', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_song_requests', to='myweb.ChurchInfo')),
            ],
        ),
    ]