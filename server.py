from rembg import remove, new_session
from rembg.session_factory import new_session

# ✨  sessione rembg con alpha‑matting
session = new_session(
    name="u2net",
    alpha_matting=True,
    alpha_matting_foreground_threshold=240,
    alpha_matting_background_threshold=10,
    alpha_matting_erode_size=2,
)

@app.route('/', methods=['POST'])
def strip():
    img_bytes = request.files['image'].read()
    out = remove(img_bytes, session=session)
    return send_file(BytesIO(out), mimetype='image/png')
