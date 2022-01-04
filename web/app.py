import os

from flask import Flask, send_file
from io import BytesIO
from functions.gan import Gan

app = Flask(__name__)

gan = Gan()

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route("/")
def hello_world():
    return "hello from ml-backend"

@app.route("/gan")
def image_world():
    img = gan.get_images()
    return serve_pil_image(img)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
