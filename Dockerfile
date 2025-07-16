FROM python:3.10-slim
WORKDIR /app
# aggiungi onnxruntime (CPU) insieme agli altri pacchetti
RUN pip install --no-cache-dir rembg pillow flask onnxruntime==1.16.3
COPY server.py .
CMD ["python", "server.py"]
