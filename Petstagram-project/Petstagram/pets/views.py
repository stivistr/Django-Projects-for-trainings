from django.shortcuts import render


# Create your views here.

def add_pet(request):
    return render(request, template_name='pet-add-page.html')


def pet_details(request):
    return render(request, template_name='pet-details-page.html')


def pet_edit(request):
    return render(request, template_name='pet-edit-page.html')


def pet_delete(request):
    return render(request, template_name='pet-delete-page.html')
