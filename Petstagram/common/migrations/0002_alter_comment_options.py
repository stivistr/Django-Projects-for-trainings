# Generated by Django 4.2.2 on 2023-06-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_time_of_publication']},
        ),
    ]
