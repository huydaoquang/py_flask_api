from flask import Flask
from user.routes import user_bp
from employee.routes import employee_bp

app = Flask(__name__)

# Đăng ký các blueprint
app.register_blueprint(user_bp)
app.register_blueprint(employee_bp)

if __name__ == '__main__':
    app.run(debug=True)
