from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):
  def setUp(self):
    self.programa = Programa(
      titulo = 'Procurando ninguém em latim',
      data_lancamento = '2003-07-04',
      tipo = 'F',
      likes = 1200,
      dislikes = 500,
    )
    self.serializer = ProgramaSerializer(instance=self.programa)

  def test_verifica_campos_serializados(self):
    """Teste que verifica os campos que estão sendo serializados"""
    data = self.serializer.data
    self.assertEqual(
      set(data.keys()), 
      set(['titulo', 'tipo', 'data_lancamento', 'likes'])
    )

  def test_verifica_conteudo_campos_serializados(self):
    """Teste que verifica o conteúdo dos campos serializados"""
    data = self.serializer.data
    self.assertEquals(data['titulo'], self.programa.titulo)
    self.assertEquals(data['data_lancamento'], self.programa.data_lancamento)
    self.assertEquals(data['tipo'], self.programa.tipo)
    self.assertEquals(data['likes'], self.programa.likes)