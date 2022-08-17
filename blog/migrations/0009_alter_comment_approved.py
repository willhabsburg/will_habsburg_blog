# Generated by Django 4.0.6 on 2022-08-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_dislikes_comment_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('post', 'Denied')], default='approved', help_text='Set to "Approved" to make this comment visible to users', max_length=10),
        ),
    ]