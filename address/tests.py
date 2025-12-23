from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from address.models import Address


class AddressDeletePermissionTest(TestCase):

    def setUp(self):

        self.user1 = User.objects.create_user(
            username='user1', password='123456'
        )

        self.user2 = User.objects.create_user(
            username='user2', password='123456'
        )

        self.address = Address.objects.create(
            user=self.user1,
            adress_name='Teste_user1',
            street='Rua A',
            number='10',
            zip_code='00000-000',
            city='Cidade A',
            district='Distrito A',
            uf='RJ'
        )

    def test_user_cannot_delete_other_users_address(self):

        self.client.login(username='user2', password='123456')

        url = reverse('delete_address', kwargs={'pk': self.address.pk})

        response = self.client.post(url)

        self.assertEqual(response.status_code, 404)

        self.assertTrue(
            Address.objects.filter(pk=self.address.pk).exists()
        )

    def test_user_owner_of_the_address_can_detele_it(self):

        self.client.login(username='user1', password='123456')

        url = reverse('delete_address', kwargs={'pk': self.address.pk})

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Address.objects.filter(pk=self.address.pk).exists()
        )