from flask import Flask
from flask_mail import Mail
import os
from flask import current_app
from flask_cors import CORS

from app.user.routes import user_bp
from app.employee.routes import employee_bp
from app.logs.routes import logs_bp
from app.mail.routes import mail_bp
from app.uploads_file.routes import uploads_bp
from app.downloads.routes import downloads_bp
from app.payment.routes import payment_bp
from app.config import Config

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})

app.config.from_object(Config)
mail = Mail(app)

with app.app_context():
    os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)

# Đăng ký các blueprint
app.register_blueprint(user_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(logs_bp)
app.register_blueprint(mail_bp)
app.register_blueprint(uploads_bp)
app.register_blueprint(downloads_bp)
app.register_blueprint(payment_bp)

if __name__ == '__main__':
    app.run(debug=True)
