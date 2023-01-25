from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
  def setUp(self):
    self.list_url = reverse('programas-list')
    self.user = User.objects.create_user('r2d2', password='123321')

  def test_autenticacao_user_com_credenciais_corretas(self):
    """Teste que verifica a autenticação de um user com credenciais corretas"""
    user = authenticate(username='r2d2', password='123321')
    self.assertTrue((user is not None) and user.is_authenticated)

  def test_requisicao_get_nao_autorizada(self):
    """Teste que verifica uma requisição GET sem autenticar"""
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_requisicao_com_username_incorreto(self):
    """Teste que verifica autenticação de user com username incorreto"""
    user = authenticate(username='r2d1', password='123321')
    self.assertFalse((user is not None) and user.is_authenticated)

  def test_requisicao_com_password_incorreta(self):
    """Teste que verifica autenticação de user com password incorreta"""
    user = authenticate(username='r2d2', password='111111')
    self.assertFalse((user is not None) and user.is_authenticated)

  def test_requisicao_get_com_user_autenticado(self):
    """Teste que verifica uma requisição GET de um user autenticado"""
    self.client.force_authenticate(self.user)
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
