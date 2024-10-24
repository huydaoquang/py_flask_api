from flask import Blueprint, request, jsonify
from flask_mail import Mail, Message
from jinja2 import Template

mail_bp = Blueprint('mail', __name__)
mail = Mail()

@mail_bp.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('to')
    otp = data.get('otp')

    # Template HTML
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            .container {
                width: 100%;
                max-width: 600px;
                margin: 20px auto;
                background: #ffffff;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                overflow: hidden;
            }
            .header {
                background: #007BFF;
                color: white;
                padding: 10px 20px;
                text-align: center;
            }
            .content {
                padding: 20px;
            }
            .footer {
                background: #f4f4f4;
                text-align: center;
                padding: 10px 20px;
                font-size: 12px;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Welcome to Our Service!</h1>
            </div>
            <div class="content">
                <p>Hello,</p>
                <p>Thank you for signing up! We are excited to have you on board.</p>
                <p>Your OTP is: <strong>{{ otp }}</strong></p>
                <p>If you have any questions, feel free to contact us!</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Your Company. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """

    # Tạo template và chèn OTP
    template = Template(html_template)
    html_content = template.render(otp=otp)

    msg = Message(subject='Your OTP Code', recipients=[recipient])
    msg.html = html_content

    try:
        mail.send(msg)
        return jsonify({"message": "Email sent!"}), 200
    except Exception as e:
        return jsonify({"message": "Failed to send email!", "error": str(e)}), 400