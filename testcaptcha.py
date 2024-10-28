from flask import Flask, render_template, request, session
from captcha.image import ImageCaptcha
import random
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Thay đổi thành một khóa bí mật thực sự

@app.route('/')
def index():
    captcha_text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5))
    session['captcha'] = captcha_text

    image_captcha = ImageCaptcha()
    image_path = os.path.join('static', 'captcha.png')
    image_captcha.write(captcha_text, image_path)

    return render_template('index.html', captcha_image=image_path)

@app.route('/verify', methods=['POST'])
def verify():
    user_input = request.form['captcha_input']
    if user_input == session.get('captcha'):
        return "Xác thực thành công!"
    else:
        return "Xác thực thất bại! Vui lòng thử lại."

if __name__ == '__main__':
    app.run(debug=True)
