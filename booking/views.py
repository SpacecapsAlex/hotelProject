from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Booking, Basket
from rooms.models import Room
from django.contrib.auth.models import User


def add_to_basket(request):
    room_id = request.POST.get('room_id')

    room = Room.objects.get(id=room_id)
    basket = Basket.objects.create(user=request.user, room=room)
    basket.save()

    return HttpResponseRedirect(reverse('room_detail', args=[room_id]))


def add_booking(request):
    return None


def get_booking(request):
    return None


def delete_booking(request):
    return None