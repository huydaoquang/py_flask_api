2xx: Thành công
200 OK: Yêu cầu đã thành công. Dữ liệu có thể được trả về.
201 Created: Tài nguyên mới đã được tạo thành công (thường dùng cho yêu cầu POST).
202 Accepted: Yêu cầu đã được chấp nhận nhưng chưa được xử lý.
204 No Content: Yêu cầu đã thành công nhưng không có nội dung nào để trả về.

3xx: Chuyển hướng
301 Moved Permanently: Tài nguyên đã được chuyển đến một địa chỉ mới vĩnh viễn.
302 Found: Tài nguyên đã được chuyển đến một địa chỉ mới tạm thời.
304 Not Modified: Tài nguyên chưa thay đổi kể từ lần yêu cầu trước đó.

4xx: Lỗi của người dùng
400 Bad Request: Yêu cầu không hợp lệ hoặc không thể xử lý.
401 Unauthorized: Yêu cầu cần xác thực, nhưng chưa có thông tin xác thực hợp lệ.
403 Forbidden: Máy chủ từ chối yêu cầu, thường do không có quyền truy cập.
404 Not Found: Tài nguyên không tìm thấy trên máy chủ.
409 Conflict: Xung đột với trạng thái hiện tại của tài nguyên (ví dụ: xóa một tài nguyên không tồn tại).

5xx: Lỗi máy chủ
500 Internal Server Error: Lỗi chung trên máy chủ, không thể xử lý yêu cầu.
502 Bad Gateway: Máy chủ nhận được phản hồi không hợp lệ từ máy chủ khác khi làm việc như một gateway.
503 Service Unavailable: Máy chủ hiện không khả dụng (do bảo trì hoặc quá tải).
504 Gateway Timeout: Thời gian chờ đã hết khi máy chủ làm việc như một gateway hoặc proxy.