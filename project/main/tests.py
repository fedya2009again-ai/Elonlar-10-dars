from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Advertisement

User = get_user_model()

class ElonTest(TestCase):
    def test_elonlar(self):
        foydalanuvchi = User.objects.create_user(username='testuser', password='123456')
        elonlar = [
            Advertisement(title='iPhone 15', description='Yangi telefon', price=800, owner=foydalanuvchi),
            Advertisement(title='MacBook Air', description='Yaxshi holatda', price=1200, owner=foydalanuvchi),
            Advertisement(title='PlayStation 5', description='Kam ishlatilgan', price=500, owner=foydalanuvchi),
            Advertisement(title='Samsung S25', description='Yangi telefon', price=700, owner=foydalanuvchi),
            Advertisement(title='Velosiped', description='Sport velosiped', price=300, owner=foydalanuvchi)
        ]
        Advertisement.objects.bulk_create(elonlar)