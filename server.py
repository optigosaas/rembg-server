from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['POST'])
def strip():
    img_bytes = request.files['image'].read()
    out_png   = remove(img_bytes)
    return send_file(BytesIO(out_png), mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
