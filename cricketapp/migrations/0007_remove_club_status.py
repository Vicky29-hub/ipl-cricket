# Generated by Django 3.2.16 on 2023-07-20 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0006_club_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='status',
        ),
    ]
