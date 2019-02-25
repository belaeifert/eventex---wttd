from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Isabela Eifert',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-999999999'
        )

    def test_create(self):
        self.obj.save()
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)