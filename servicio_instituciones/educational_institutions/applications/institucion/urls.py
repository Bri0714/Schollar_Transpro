from django.urls import path
from .views import ListInstituciones, InstitucionRetrieveUpdateDestroyView

app_name = 'institucion_app'

urlpatterns = [
    # Ruta para la página principal
    path('instituciones/', ListInstituciones.as_view(), name='lista-instituciones'),
    path('instituciones/<int:pk>/', InstitucionRetrieveUpdateDestroyView.as_view(), name='institucion-detail'),
]
