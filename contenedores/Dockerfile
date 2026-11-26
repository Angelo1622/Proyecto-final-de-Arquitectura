# 1. Imagen base (oficial y liviana)
FROM python:3.12-alpine

# 2. Carpeta de trabajo
WORKDIR /usr/src/app

# 3. Copiar dependencias e instalarlas
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
COPY app/ ./

# 5. Puerto que expone el servicio
EXPOSE 5000

# 6. Comando que arranca la aplicación
CMD ["python", "app.py"]
