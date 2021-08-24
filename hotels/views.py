from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from hotels.models import Guests, Rooms, Hotels, description_list
from hotels.serializers import GuestsSerializer, RoomSerializer, HotelsSerializer


def index(request):

    hotel = Hotels.objects.all()
    room = Rooms.objects.all()
    desc = description_list.objects.all()

    data = {
        'hotels': hotel,
        'rooms': room,
        'description': desc,
    }

    return render(request, "hotels/web/index.html", data)


def rooms(request):
    return render(request, "hotels/web/rooms.html")


def reservation(request):
    return render(request, "hotels/web/reservation.html")


def activities(request):
    return render(request, "hotels/web/activities.html")


def contact(request):
    return render(request, "hotels/web/contact.html")


def details(request):
    return render(request, "hotels/web/details.html")


class GusestsList(APIView):

    serializer_class = GuestsSerializer

    def get_queryset(self):
        quest = Guests.objects.all()
        return quest

    def get(self, request, *arg, **kwarg):
        return Response(request.data)

    def post(self, request, *arg, **kwarg):

        hotel = request.data["hotel_name_number"]
        ct = Guests.objects.filter(hotel_name_number=hotel).count()

        return Response(request.data)


class GetRoomsView(generics.ListCreateAPIView):

    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny, )

class GetHotelsView(generics.ListCreateAPIView):

    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = (AllowAny, )
