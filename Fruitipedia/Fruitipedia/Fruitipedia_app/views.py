from django.shortcuts import render, redirect
from .forms import CreateProfileForm, CreateFruitForm, DeleteFruitForm, EditProfileForm
from .models import Profile, Fruit


# Create your views here.

def index_page(request):
    return render(request, template_name='index.html')


def dashboard(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, template_name='dashboard.html', context=context)


def create_fruit(request):
    profile = Profile.objects.first()
    form = CreateFruitForm()

    if request.method == 'POST':
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template_name='create-fruit.html', context=context)


def fruit_details(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = Profile.objects.first()

    context = {
        'fruit': fruit,
        'profile': profile,
    }

    return render(request, template_name='details-fruit.html', context=context)


def fruit_edit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {
            'form': CreateFruitForm(initial=fruit.__dict__),
            'profile': profile,
        }
        return render(request, template_name='edit-fruit.html', context=context)
    else:
        form = CreateFruitForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template_name='edit-fruit.html', context=context)


def fruit_delete(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = Profile.objects.first()

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    form = DeleteFruitForm(instance=fruit)
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template_name='delete-fruit.html', context=context)


def create_profile(request):
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'add_form': form,
    }

    return render(request, template_name='create-profile.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    all_fruits = len(Fruit.objects.all())

    context = {
        'profile': profile,
        'all_fruits': all_fruits,
    }

    return render(request, template_name='details-profile.html', context=context)


def profile_edit(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {
            'form': EditProfileForm(initial=profile.__dict__),
            'profile': profile,
        }
        return render(request, template_name='edit-profile.html', context=context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template_name='edit-profile.html', context=context)


def profile_delete(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()

    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, template_name='delete-profile.html', context=context)
