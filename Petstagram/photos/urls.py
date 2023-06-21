from django.urls import path, include
from Petstagram.photos import views

urlpatterns = [
    path('add', views.add_photo, name='photo-add'),
    path('<int:pk>/', include([
        path('', views.details_photo, name='photo-details'),
        path('edit/', views.edit_photo, name='photo-edit'),
        path('delete/', views.delete_photo, name='delete-photo'),
    ]))
]
