# Generated by Django 3.2.12 on 2022-04-19 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_auto_20220420_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedin_url',
        ),
    ]