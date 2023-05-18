from django.test import TestCase
from restaurant.models import Menu 
from restaurant.models import Booking

class MenuTest(TestCase):
  def test_menu(self):
    menu = Menu.objects.create(name='Pizza', price=8, description='very nice')
    self.assertEqual(str(menu), 'Pizza')

class BookingTest(TestCase):
  def test_booking(self):
    booking = Booking.objects.create(first_name = 'Leon')
    self.assertEqual(str(Booking),'Leon')
