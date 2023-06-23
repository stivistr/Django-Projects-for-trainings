# Generated by Django 4.2.2 on 2023-06-22 08:35

import django.core.validators
from django.db import migrations, models
import myplant_project.myplant_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('outdoor', 'Outdoor Plants'), ('indoor', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), myplant_project.myplant_app.validators.NameContainsOnlyLetters()])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[myplant_project.myplant_app.validators.NameStartsWithCapital()])),
                ('last_name', models.CharField(max_length=20, validators=[myplant_project.myplant_app.validators.NameStartsWithCapital()])),
                ('profile_picture', models.URLField(blank=True)),
            ],
        ),
    ]