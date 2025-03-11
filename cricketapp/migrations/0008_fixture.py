# Generated by Django 3.2.16 on 2023-07-20 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapp', '0007_remove_club_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('venue', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(default='Scheduled', max_length=20, null=True)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('team1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1_fixtures', to='cricketapp.club')),
                ('team2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2_fixtures', to='cricketapp.club')),
            ],
        ),
    ]
