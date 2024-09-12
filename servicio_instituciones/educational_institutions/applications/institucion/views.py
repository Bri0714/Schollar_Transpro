from django.shortcuts import render
#from django.http import JsonResponse
from rest_framework import generics
from .serializers import InstitucionSerializer
from .models import Institucion
# Create your views here.

#def saludar(request):
#   return JsonResponse({'saludo': 'hola'})

class ListInstituciones(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    
# Vista para ver, actualizar o eliminar una institución individual
class InstitucionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer