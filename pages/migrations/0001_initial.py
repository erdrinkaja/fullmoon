# Generated by Django 4.1 on 2022-08-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('event_status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('data', models.DateTimeField(primary_key=True, serialize=False)),
                ('status', models.IntegerField()),
                ('phase', models.IntegerField()),
                ('day_discription', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MoonPhase',
            fields=[
                ('moon_phase', models.IntegerField(primary_key=True, serialize=False)),
                ('moon_image', models.ImageField(upload_to=None)),
                ('description_1', models.TextField()),
                ('description_2', models.TextField()),
                ('description_3', models.TextField()),
            ],
        ),
    ]