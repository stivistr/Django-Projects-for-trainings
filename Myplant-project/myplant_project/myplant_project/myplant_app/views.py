from django.shortcuts import render, redirect
from myplant_project.myplant_app.models import Profile, Plant
from .forms import CreateProfileForm, CreatePlantForm, DeletePlantForm, EditProfileForm


# Create your views here.

def home_page(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }
    if not profile:
        return render(request, template_name='home-page.html')

    return render(request, template_name='home-page.html', context=context)


def create_profile(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'create_form': form,
    }

    return render(request, template_name='create-profile.html', context=context)


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
    }

    return render(request, template_name='catalogue.html', context=context)


def create_plant(request):
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form,
    }

    return render(request, template_name='create-plant.html', context=context)


def plant_details(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    form = CreatePlantForm()

    if request.method == 'GET':
        form = CreatePlantForm(request.GET)

    context = {
        'plant': plant,
        'form': form,
    }

    return render(request, template_name='plant-details.html', context=context)


def edit_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)

    if request.method == 'GET':
        context = {'form': CreatePlantForm(initial=plant.__dict__)}
        return render(request, template_name='edit-plant.html', context=context)
    else:
        form = CreatePlantForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'form': form}
            return render(request, template_name='edit-plant.html', context=context)


def delete_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    form = DeletePlantForm(instance=plant)
    context = {'form': form}

    return render(request, template_name='delete-plant.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    all_plants = Plant.objects.all()

    context = {
        'profile': profile,
        'all_plants': all_plants,
    }

    return render(request, template_name='profile-details.html', context=context)


def profile_edit(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        context = {'form': EditProfileForm(initial=profile.__dict__)}
        return render(request, template_name='edit-profile.html', context=context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')
        else:
            context = {'form': form}
            return render(request, template_name='edit-profile.html', context=context)


def profile_delete(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('home-page')

    return render(request, template_name='delete-profile.html')
