from django.db import models
from django.core.validators import MinLengthValidator
from myplant_project.myplant_app.validators import NameStartsWithCapital, NameContainsOnlyLetters


# Create your models here.

class Profile(models.Model):
    username = models.CharField( max_length=10, validators=[MinLengthValidator(2)], blank=False, null=False)
    first_name = models.CharField(max_length=20, validators=[NameStartsWithCapital()], blank=False, null=False)
    last_name = models.CharField(max_length=20, validators=[NameStartsWithCapital()], blank=False, null=False)
    profile_picture = models.URLField(blank=True, null=True)


class Plant(models.Model):
    CHOICES = [('outdoor', 'Outdoor Plants'), ('indoor', 'Indoor Plants')]

    plant_type = models.CharField(max_length=14, choices=CHOICES)
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), NameContainsOnlyLetters()])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    #profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

