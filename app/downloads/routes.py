from flask import Blueprint, send_file,render_template
import pandas as pd
from io import BytesIO
import zipfile

downloads_bp = Blueprint('downloads', __name__)

@downloads_bp.route('/download')
def download():
    return render_template('download_csv.html')

@downloads_bp.route('/download_csv', methods=['GET'])
def download_csv():
    # Dữ liệu tự định nghĩa (ví dụ: danh sách từ điển)
    data = [
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"}
    ]

    # Tạo DataFrame từ dữ liệu
    df = pd.DataFrame(data)

    # Lưu DataFrame vào BytesIO
    csv_file = BytesIO()
    df.to_csv(csv_file, index=False)
    csv_file.seek(0)  # Đặt con trỏ về đầu tệp để đọc

    # Gửi tệp CSV về phía client
    return send_file(csv_file, as_attachment=True, download_name='data.csv', mimetype='text/csv')


@downloads_bp.route('/download_multiple')
def download_multiple():
    return render_template('download_multiple_csv.html')

@downloads_bp.route('/download_multiple_files', methods=['GET'])
def download_multiple_files():
    # Giả lập nhiều tệp dữ liệu
    data_sets = {
        "data1": [{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}],
        "data2": [{"Product": "Laptop", "Price": 1000}, {"Product": "Phone", "Price": 500}],
        "data3": [{"Product": "Laptop", "Price": 1000}, {"Product": "Phone", "Price": 500}],
        "data4": [{"Product": "Laptop", "Price": 1000}, {"Product": "Phone", "Price": 500}],
        "data5": [{"Product": "Laptop", "Price": 1000}, {"Product": "Phone", "Price": 500}],
        "data6": [{"Product": "Laptop", "Price": 1000}, {"Product": "Phone", "Price": 500}],
        "data7": [{"Product": "Laptop", "Price": 1000}, {"Product": "Phone", "Price": 500}],
    }

    zip_buffer = BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for name, data in data_sets.items():
            df = pd.DataFrame(data)
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)
            zip_file.writestr(f'{name}.csv', csv_buffer.read())
    
    zip_buffer.seek(0)
    return send_file(zip_buffer, as_attachment=True, download_name='data_files.zip', mimetype='application/zip')
