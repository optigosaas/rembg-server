FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir rembg pillow flask
COPY server.py .
CMD ["python", "server.py"]
