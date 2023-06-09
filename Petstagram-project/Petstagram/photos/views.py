from django.shortcuts import render


# Create your views here.

def add_photo(request):
    return render(request, template_name='photo-add-page.html')


def details_photo(request):
    return render(request, template_name='photo-details-page.html')


def edit_photo(request):
    return render(request, template_name='photo-edit-page.html')
