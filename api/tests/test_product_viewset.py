import pytest

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from api.factories import UserFactory
from api.models import Product


@pytest.mark.django_db
class TestProductViewSet(APITestCase):

    # Criando uma instância de Product para os testes
    def setUp(self):
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        token.save()

        self.list_url = reverse('product-list', kwargs={'version': 'v1'})
        self.product = Product.objects.create(
            title='World of Warcraft Shadowlands',
            description='Expansão "Shadowlands" para o jogo base World of Warcraft.',
            price=150,
        )


    # Testando se o get da listagem dos produtos irá retornar status 200
    def test_list_products(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Testando se o post de um novo produto irá retornar 201
    def test_create_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        data = {
            'title': 'World of Warcraft (1 mo.)',
            'description': 'Adiciona 1 mês de assinatura à conta.',
            'price': '35'
        }

        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)