from rest_framework.routers import DefaultRouter
from .views import RutaListCreate

app_name = 'ruta_app'

router = DefaultRouter()
router.register(r'rutas', RutaListCreate, basename='ruta')

urlpatterns = router.urls
