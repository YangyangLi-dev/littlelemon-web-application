from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import views, viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from .permissions import IsAdmin, IsManager, IsCustomer, ReadOnly
# Create your views here.

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_items = Menu.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)


def display_menu_item(request, pk):
    menu_item = Menu.objects.filter(pk=pk).first()
    context = {'menu_item': menu_item}
    return render(request, 'menu_item.html', context)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin | IsManager]
        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_permissions(self):
        if self.request.method in ["GET","POST"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin | IsManager]
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer            