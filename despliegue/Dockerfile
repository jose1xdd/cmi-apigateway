# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el contenido del proyecto al contenedor
COPY . .

# Instala dependencias si es necesario (ejemplo con Flask)
RUN pip install flask

# Expone el puerto que usará la app
EXPOSE 5000

# Define el comando por defecto para ejecutar
CMD ["python", "-m", "http.server", "5000"]
