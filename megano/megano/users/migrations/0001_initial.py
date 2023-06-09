# Generated by Django 4.1.7 on 2023-03-23 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profiles', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('fullName', models.CharField(max_length=128, verbose_name='Ф.И.О.')),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=64, verbose_name='телефон')),
                ('avatar', models.FileField(blank=True, null=True, upload_to=users.models.upload_profile_avatar, verbose_name='аватар')),
            ],
        ),
    ]
