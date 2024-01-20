from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Codeur code'},
#     {'id': 2, 'name': 'Frontend Guru'},
#     {'id': 3, 'name': 'Design with Dav!'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)
