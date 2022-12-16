from django.contrib import admin
from django.urls import path, include
from camilinda.views import AtividadesViewSet, RelatorioViewSet, ListaRelatorioAtividade
from rest_framework import routers

# aqui eu vou definir a rota principal
router = routers.DefaultRouter()
# e vou registrar AtividadesViewSet
router.register('atividades', AtividadesViewSet, basename='Atividades')
router.register('relatorios', RelatorioViewSet, basename='Relatorios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('atividade/<int:pk>/relatorios/', ListaRelatorioAtividade.as_view())
]
