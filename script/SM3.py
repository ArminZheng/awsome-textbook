from gmssl import sm3, func
# 消息体
data = b'1234'
# sm3 hash算法，可用于签名消息体
print(sm3.sm3_hash(func.bytes_to_list(data)))