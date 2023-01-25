from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from aluraflix.views import ProgramaViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Aluraflix",
      default_version='v1',
      description="Serviço de Streaming desenvolvido na formação Alura de Django Rest Framework",
      terms_of_service="#",
      contact=openapi.Contact(email="rd2d@alura.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('programas', ProgramaViewSet, basename='programas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(
        'swagger/', 
        schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'
    ),
    path(
        'redoc/', 
        schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'
    ),
]
