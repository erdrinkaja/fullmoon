# Generated by Django 4.1 on 2022-08-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0004_remove_event_date_created_remove_event_date_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moon',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='moon',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='moon',
            name='deleted',
        ),
        migrations.AlterField(
            model_name='moon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]