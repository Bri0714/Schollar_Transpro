from rest_framework import serializers
import requests
from rest_framework.exceptions import ValidationError
from .models import Ruta

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

    def validate_institucion_id(self, value):
        # Verificar que el ID de la institución es positivo
        if value <= 0:
            raise ValidationError('El ID de la institución debe ser un valor positivo.')

        # Verificar si la institución existe en el servicio de instituciones
        url = f'http://servicio_instituciones:8000/api/instituciones/{value}/'
        
        # Agregar print statements para debuggear la solicitud
        print(f'Intentando acceder a: {url}')
        try:
            response = requests.get(url, timeout=5)
            print(f'Respuesta del servicio de instituciones: Status code {response.status_code}')
            print(f'Contenido de la respuesta: {response.text}')
            
            if response.status_code != 200:
                raise ValidationError('La institución educativa especificada no existe.')
        except requests.ConnectionError:
            print('Error de conexión con el servicio de instituciones.')
            raise ValidationError('Error de conexión con el servicio de instituciones.')
        except requests.Timeout:
            print('Tiempo de espera agotado al conectar con el servicio de instituciones.')
            raise ValidationError('Tiempo de espera agotado al conectar con el servicio de instituciones.')
        except requests.RequestException as e:
            print(f'Error al verificar la institución: {str(e)}')
            raise ValidationError(f'Error al verificar la institución: {str(e)}')

        return value