from django.shortcuts import render, redirect
from Petstagram.pets.models import Pet
from Petstagram.pets.forms import PetForm, PetDeleteForm
from Petstagram.common.forms import CommentForm


# Create your views here.

def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, template_name='pet-add-page.html', context=context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = pet
            comment.save()

            return redirect(request.META['HTTP_REFERER'] + f'#{pet_slug}')

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, template_name='pet-details-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)
    context = {'form': form}

    return render(request, template_name='pet-edit-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}

    return render(request, template_name='pet-delete-page.html', context=context)
