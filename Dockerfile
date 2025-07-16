FROM python:3.10-slim
WORKDIR /app

# ← Aggiungi numpy<2.0 PRIMA di onnxruntime
RUN pip install --no-cache-dir "numpy<2.0" onnxruntime==1.16.3 \
    rembg pillow flask

COPY server.py .
CMD ["python", "server.py"]
