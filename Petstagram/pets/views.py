from django.shortcuts import render
from Petstagram.pets.models import Pet

# Create your views here.

def add_pet(request):
    return render(request, template_name='pet-add-page.html')


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, template_name='pet-details-page.html', context=context)


def pet_edit(request):
    return render(request, template_name='pet-edit-page.html')


def pet_delete(request):
    return render(request, template_name='pet-delete-page.html')
