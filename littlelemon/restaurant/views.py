from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

def home(request):
  return render(request, 'index.html', {})
class MenuItemsView(generics.ListCreateAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

  def get_permissions(self):
    if(self.request.method!='GET'):
        return [IsAuthenticated(), IsAdminUser()]
    return []

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

  def get_permissions(self):
    if(self.request.method!='GET'):
        return [IsAuthenticated(), IsAdminUser()]
    return []

class BookingsView(generics.ListCreateAPIView):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]
