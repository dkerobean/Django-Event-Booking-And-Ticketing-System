# Generated by Django 4.1.3 on 2022-12-07 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_gps_location_alter_event_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_at']},
        ),
    ]
