from rest_framework import viewsets, generics, status
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunosSerializer, AlunosSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class AlunosViewset(viewsets.ModelViewSet):
  """Exibe todos os alunos e alunos"""
  queryset = Aluno.objects.all()
  serializer_class = AlunosSerializer
  def get_serializer_class(self):
    if self.request.version == 'v2':
      return AlunosSerializerV2
    else:
      return AlunosSerializer

class CursosViewset(viewsets.ModelViewSet):
  """Exibe todos os cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  http_method_names = ['GET', 'POST', 'PUT', 'PATCH']

  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      response = Response(serializer.data, status=status.HTTP_201_CREATED)
      id = str(serializer.data['id'])
      response['Location'] = request.build_absolute_url() + id
      return response

class MatriculasViewset(viewsets.ModelViewSet):
  """Exibe todos os Matriculas"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
  http_method_names = ['get', 'post', 'put', 'patch']

  @method_decorator(cache_page(20))
  def dispatch(self, request, *args, **kwargs):
    return super(MatriculasViewset, self).dispatch(*args, **kwargs)

class ListaMatriculasAluno(generics.ListAPIView):
  """Lista as matrículas de um aluno ou aluno"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
  """Lista alunos e alunas matriculados em um curso"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaAlunosMatriculadosSerializer