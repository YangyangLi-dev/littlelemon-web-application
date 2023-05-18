from django.test import TestCase
from datetime import date

from restaurant.models import Menu, Booking
from restaurant.serializer import MenuSerializer, BookingSerializer


# Create your tests here.
class MenuViewSetTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Pizza", price=80)
    
    def test_get_all(self):
        items =  Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        self.assertEqual(len(serialized_items.data), 1)


class BookingViewSetTest(TestCase):
    def setUp(self):
        Booking.objects.create(first_name="Leon", booking_date=date.today())
    
    def test_get_all(self):
        items =  Booking.objects.all()
        serialized_items = BookingSerializer(items, many=True)
        self.assertEqual(len(serialized_items.data), 1)
