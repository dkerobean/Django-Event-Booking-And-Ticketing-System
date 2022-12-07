# Generated by Django 4.1.3 on 2022-12-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_rename_ticket_number_event_total_tickets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='total_tickets',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
