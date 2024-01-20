from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('room/create/', views.createRoom, name='create_room'),
    path('room/<str:pk>/update/', views.updateRoom, name='update_room'),
    path('room/<str:pk>/delete/', views.deleteRoom, name='delete_room'),
    path('room/<str:pk>/', views.room, name='room'),
]