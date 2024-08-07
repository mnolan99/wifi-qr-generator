from flask import Flask, render_template, request, send_file
import wifi_qrcode_generator as qr
from PIL import Image
import io

app = Flask(__name__, static_url_path='/static')

def generate_wifi_qr(ssid, password, auth_type):
    qr_code = qr.wifi_qrcode(ssid, hidden=False, authentication_type=auth_type, password=password)
    img = qr_code.make_image(fill='black', back_color='white')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ssid = request.form['ssid']
        password = request.form['password']
        auth_type = request.form['auth_type']
        qr_code_io = generate_wifi_qr(ssid, password, auth_type)
        return send_file(qr_code_io, mimetype='image/png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)