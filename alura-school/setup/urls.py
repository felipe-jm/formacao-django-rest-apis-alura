from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewset, CursosViewset, MatriculasViewset, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf.urls.static import static
from setup import settings

router = routers.DefaultRouter()
router.register('alunos', AlunosViewset, basename='alunos')
router.register('cursos', CursosViewset, basename='cursos')
router.register('matriculas', MatriculasViewset, basename='matriculas')

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('acesso-secreto-ao-admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
