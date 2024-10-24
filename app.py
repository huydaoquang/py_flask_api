from flask import Flask
from flask_mail import Mail

from app.user.routes import user_bp
from app.employee.routes import employee_bp
from app.logs.routes import logs_bp
from app.mail.routes import mail_bp
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

# Đăng ký các blueprint
app.register_blueprint(user_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(logs_bp)
app.register_blueprint(mail_bp)

if __name__ == '__main__':
    app.run(debug=True)
