# Generated by Django 4.2.13 on 2024-05-25 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Star', 'Star'), ('Square', 'Square'), ('Circle', 'Circle')], max_length=50)),
                ('coordinates', models.JSONField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
