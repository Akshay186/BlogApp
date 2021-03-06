# Generated by Django 3.2.12 on 2022-04-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0012_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='_/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Add blog post snippet here, so that users understand what the post is about.', max_length=255),
        ),
    ]
