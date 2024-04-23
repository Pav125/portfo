# Generated by Django 5.0.4 on 2024-04-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_logo',
            field=models.ImageField(blank=True, null=True, upload_to='github_logo/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gmail_logo',
            field=models.ImageField(blank=True, null=True, upload_to='gmail_logo/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_logo',
            field=models.ImageField(blank=True, null=True, upload_to='linkedin_logo/'),
        ),
    ]
