from flask import Flask, request, send_file
from rembg import remove
from rembg.session_factory import new_session
from io import BytesIO
import os

# ── Flask app ----------------------------------------------------
app = Flask(__name__)

# ── rembg session con alpha‑matting meno aggressivo --------------
session = new_session(
    name="u2net",                        # oppure "u2net_human_seg"
    alpha_matting=True,
    alpha_matting_foreground_threshold=240,
    alpha_matting_background_threshold=10,
    alpha_matting_erode_size=2,
)

# ── Endpoint POST ------------------------------------------------
@app.route("/", methods=["POST"])
def strip():
    img_bytes = request.files["image"].read()
    out_png   = remove(img_bytes, session=session)
    return send_file(BytesIO(out_png), mimetype="image/png")

# ── Avvio --------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
