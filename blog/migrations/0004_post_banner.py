# Generated by Django 4.0.6 on 2022-07-31 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, help_text='A banner image for the post', null=True, upload_to=''),
        ),
    ]
