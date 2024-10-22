import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def check_refresh_token(username):
    # Lấy giá trị từ Redis
    token = redis_client.get(f'{username}')
    
    if token:
        return token.decode('utf-8')  
    else:
        return None  

username = 'huydaoquang'
token = check_refresh_token(username)

if token:
    print(f'refresh_token: {token}')
else:
    print('Token not found.')


# Xóa key
# result = redis_client.delete(f'refresh_token:{username}')

# if result == 1:
#     print(f"Key '{redis_client}' đã được xóa.")
# else:
#     print(f"Key '{redis_client}' không tồn tại.")