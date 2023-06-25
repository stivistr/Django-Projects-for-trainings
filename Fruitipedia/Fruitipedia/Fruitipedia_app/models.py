from django.db import models
from django.core.validators import MinLengthValidator
from .validators import FirstCharMustBeLetterValidator, NameContainsOnlyLettersValidator


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=[MinLengthValidator(2), FirstCharMustBeLetterValidator()])
    last_name = models.CharField(max_length=35, validators=[MinLengthValidator(1), FirstCharMustBeLetterValidator()])
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    image_url = models.URLField(blank=True, null=True)
    age = models.IntegerField(default=18, null=True)


class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2), NameContainsOnlyLettersValidator()])
    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    nutrition = models.TextField(blank=True, null=True)
