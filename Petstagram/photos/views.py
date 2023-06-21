from django.shortcuts import render, redirect
from Petstagram.photos.models import Photo
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.common.forms import CommentForm

# Create your views here.

def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form}

    return render(request, template_name='photo-add-page.html', context=context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

            return redirect(request.META['HTTP_REFERER'] + f'#{photo.pk}')

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }

    return render(request, template_name='photo-details-page.html', context=context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('photo-details', pk)
    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_name='photo-edit-page.html', context=context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()

    return redirect('index')
