# Usa la imagen oficial de Python 3 como base
FROM python:3.10-slim

# Copia todo el contenido de la carpeta actual al directorio /usr/src/app dentro del contenedor
COPY . /usr/src/app

# Establece el directorio de trabajo dentro del contenedor como la carpeta donde están los archivos copiados
WORKDIR /usr/src/app

# Instala las dependencias desde el archivo requirements/local.txt
RUN pip install --no-cache-dir -r requirements/local.txt

# Expone el puerto 8001
EXPOSE 8001

# Comando que se ejecutará cuando el contenedor inicie
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
