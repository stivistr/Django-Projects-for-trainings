from django.contrib import admin
from Petstagram.pets.models import Pet


# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Pet, PetAdmin)
