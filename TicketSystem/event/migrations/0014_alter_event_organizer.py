# Generated by Django 4.1.3 on 2022-12-14 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_profile_image'),
        ('event', '0013_alter_event_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.profile'),
        ),
    ]
