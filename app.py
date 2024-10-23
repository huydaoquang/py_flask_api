from flask import Flask
from app.user.routes import user_bp
from app.employee.routes import employee_bp
from app.logs.routes import logs_bp
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Đăng ký các blueprint
app.register_blueprint(user_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(logs_bp)

if __name__ == '__main__':
    app.run(debug=True)
