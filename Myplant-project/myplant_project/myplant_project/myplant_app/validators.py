from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class NameStartsWithCapital:
    def __call__(self, value):
        if not value[0].isupper():
            raise ValidationError("Your name must start with a capital letter!")

    def __eq__(self, other):
        return True


@deconstructible
class NameContainsOnlyLetters:
    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError("Plant name should contain only letters!")

    def __eq__(self, other):
        return True
