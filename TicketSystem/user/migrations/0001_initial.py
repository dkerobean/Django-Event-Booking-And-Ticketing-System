# Generated by Django 4.1.3 on 2022-12-03 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, max_length=400, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profile-imgs/avatar.svg', null=True, upload_to='profiles')),
                ('background_image', models.ImageField(blank=True, default='background-imgs/default.jpg', null=True, upload_to='backgrounds')),
                ('social_website', models.CharField(blank=True, max_length=300, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=300, null=True)),
                ('social_facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('social_instagram', models.CharField(blank=True, max_length=300, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
