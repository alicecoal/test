# Generated by Django 3.0.5 on 2021-06-03 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='signup_confirmation',
            field=models.BooleanField(default=True),
        ),
    ]
