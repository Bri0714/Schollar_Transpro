from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .models import Ruta
from .serializers import RutaSerializer
import requests

class RutaListCreate(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

    def create(self, request, *args, **kwargs):
        institucion_id = request.data.get('institucion_id')
        
        # Validar que se envió el campo institucion_id
        if not institucion_id:
            print('Error: El campo "institucion_id" es requerido.')
            raise ValidationError({'institucion_id': 'El campo "institucion_id" es requerido.'})

        # Validar que institucion_id sea un entero válido
        try:
            institucion_id = int(institucion_id)
        except ValueError:
            print(f'Error: El ID de la institución debe ser un número entero. Se recibió: {institucion_id}')
            raise ValidationError({'institucion_id': 'El ID de la institución debe ser un número entero.'})

        # Validar si el ID de la institución es positivo
        if institucion_id <= 0:
            print(f'Error: El ID de la institución debe ser un valor positivo. Se recibió: {institucion_id}')
            raise ValidationError({'institucion_id': 'El ID de la institución debe ser un valor positivo.'})

        # Verificar si la institución existe en el servicio de instituciones
        url = f'http://servicio_instituciones:8000/api/instituciones/{institucion_id}/'
        print(f'Intentando acceder a: {url}')
        
        try:
            response = requests.get(url, timeout=5)
            print(f'Respuesta del servicio de instituciones: Status code {response.status_code}')
            print(f'Contenido de la respuesta: {response.text}')

            if response.status_code != 200:
                print(f'Error: La institución con ID {institucion_id} no fue encontrada.')
                raise ValidationError({'institucion_id': 'La institución educativa especificada no existe.'})

        except requests.ConnectionError:
            print('Error de conexión con el servicio de instituciones.')
            raise ValidationError({'institucion_id': 'Error de conexión con el servicio de instituciones.'})
        except requests.Timeout:
            print('Tiempo de espera agotado al conectar con el servicio de instituciones.')
            raise ValidationError({'institucion_id': 'Tiempo de espera agotado al conectar con el servicio de instituciones.'})
        except requests.RequestException as e:
            print(f'Error al verificar la institución: {str(e)}')
            raise ValidationError({'institucion_id': f'Error al verificar la institución: {str(e)}'})

        # Si todo está bien, proceder con la creación del registro
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        print('Obteniendo la lista de rutas...')
        return super().list(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        print('Actualizando una ruta...')
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        print('Eliminando una ruta...')
        return super().destroy(request, *args, **kwargs)
    
    
    #def perform_create(self, serializer):
    #    institucion_id = self.request.data.get('institucion_id')
    #    
    #    print(f'Intentando crear ruta con institucion_id: {institucion_id}')
    #    
    #    if not institucion_id:
    #        print('Error: El campo "institucion_id" es requerido.')
    #        raise ValidationError({'institucion_id': 'Este campo es requerido.'})
#
    #    try:
    #        # Agrega un print aquí para verificar el URL antes de hacer la solicitud
    #        url = f'http://servicio_instituciones:8000/api/instituciones/{institucion_id}/'
    #        print(f'Intentando acceder a: {url}')
    #        
    #        response = requests.get(url, timeout=5)
    #        
    #        print(f'Respuesta del servicio de instituciones: Status code {response.status_code}')
    #        print(f'Contenido de la respuesta: {response.text}')
    #        
    #        if response.status_code == 200:
    #            print(f'Institución {institucion_id} verificada correctamente')
    #            serializer.save()
    #            print('Ruta guardada exitosamente')
    #        else:
    #            print(f'Institución {institucion_id} no encontrada. Status code: {response.status_code}')
    #            raise ValidationError({'institucion_id': 'La institución educativa especificada no existe.'})
    #    
    #    except requests.ConnectionError:
    #        print('Error de conexión con el servicio de instituciones')
    #        raise ValidationError({'error': 'Error de conexión con el servicio de instituciones.'})
    #    except requests.Timeout:
    #        print('Timeout al conectar con el servicio de instituciones')
    #        raise ValidationError({'error': 'Tiempo de espera agotado al conectar con el servicio de instituciones.'})
    #    except requests.RequestException as e:
    #        print(f'Error al verificar la institución: {str(e)}')
    #        raise ValidationError({'error': 'Error al verificar la institución. Por favor, intente más tarde.'})
