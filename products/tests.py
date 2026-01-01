from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from products.models import Product, Department


class ProductTest(TestCase):

    def setUp(self):
        
        self.user1 = User.objects.create_superuser(
            username='user1', password='123456'
        )

        self.user2 = User.objects.create_user(
            username='user2', password='123456'
        )
    
    def test_normal_user_cannot_create_a_product(self):

        self.client.login(username='user2', password='123456')

        url = reverse('new_product')

        department = Department.objects.create(name='TESTE')
        response = self.client.post(url, {
            'name': 'Teste',
            'barcode': '123456789',
            'price': '11.99',
            'department': department.pk
        })

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Product.objects.count(), 0)

    def test_superuser_can_add_a_procuct(self):
        
        self.client.login(username='user1', password='123456')

        url = reverse('new_product')

        department = Department.objects.create(name='TESTE')
        response = self.client.post(url, {
            'name': 'Teste',
            'bar_code': '123456789',
            'price': 11.99,
            'department': department.pk
        }, follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.count(), 1)


    def test_normal_user_cannot_edit_a_product(self):
        
        self.client.login(username='user2', password='123456')

        department = Department.objects.create(name='TESTE')
        product = Product.objects.create(
            name='Teste',
            bar_code='123456789',
            price=10,
            department=department
        )

        url = reverse('product_update', kwargs={'pk': product.pk})

        response = self.client.post(url, {
            'name': 'Teste2',
            'bar_code': '000000000',
            'price': 10.99,
            'department': department.pk
        })

        self.assertEqual(response.status_code, 403)

    def test_superuser_can_edit_a_product(self):
        
        self.client.login(username='user1', password='123456')


        department = Department.objects.create(name='TESTE')
        product = Product.objects.create(
            name='Teste',
            bar_code='123456789',
            price=10,
            department=department
        )

        url = reverse('product_update', kwargs={'pk': product.pk})

        response = self.client.post(url, {
            'name': 'Modificado',
            'bar_code': '000000000',
            'price': 10.99,
            'department': department.pk
        }, follow=True)

        self.assertEqual(response.status_code, 200)