# Generated by Django 4.2.2 on 2023-06-22 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myplant_app', '0003_alter_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myplant_app.profile'),
            preserve_default=False,
        ),
    ]
