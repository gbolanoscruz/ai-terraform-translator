# Usar una imagen oficial y ligera de Python
FROM python:3.12-slim-trixie

# Aplicamos parches de seguridad pendientes de Debian y limpiamos caché
RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar primero los requerimientos para aprovechar el caché de Docker
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto que usa Streamlit
EXPOSE 8501

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Comando para levantar la aplicación
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]