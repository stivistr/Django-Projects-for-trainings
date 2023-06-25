from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FirstCharMustBeLetterValidator:
    def __call__(self, value):
        if not value[0].isalpha():
            raise ValidationError("Your name must start with a letter!")


@deconstructible
class NameContainsOnlyLettersValidator:
    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError("Fruit name should contain only letters!")