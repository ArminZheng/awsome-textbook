# 国密即国家密码局认定的国产密码算法。主要有SM1，SM2，SM3，SM4。
## 目前SM1算法没有公开，只能集成在芯片中。目前应用较多的是SM2、SM3和SM4算法，这三者用法不一
## SM2 (非对)属于非对称加密算法，使用公钥加密，私钥解密，在安全性和运算速度方面要优于RSA算法
## SM3 (MD5)属于不可逆加密算法，类似于md5，常用于签名
## SM4 (对称)属于对称加密算法，可用于替代DES/AES等国际算法, SM4算法与AES算法具有相同的密钥长度和分组长度，都是128位
from gmssl import sm2, func, sm3, sm4 # GmSSL是一个开源的加密包的python实现; BSD开源许可证

# 私钥
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
# 公钥
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
# 声明一个sm2对象
sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)

def SM2(): # 由国家密码管理局与 2010-12 公布
    # 消息体
    data = b"111"
    # 加密
    enc_data = sm2_crypt.encrypt(data)
    print(enc_data)
    # 解密
    dec_data =sm2_crypt.decrypt(enc_data)
    print(dec_data)
    # 断言解密之后得到原消息体
    assert dec_data == data
    print(dec_data == data)

    # 消息体
    data = b"111" # bytes类型
    # 调用sm3签名
    sign = sm2_crypt.sign(data, "3") #  16进制
    # sm3校验签名
    assert sm2_crypt.verify(sign, data)
    print(sign)
    print(sm2_crypt.verify(sign, data))

SM2()

# a97f7cd4b3c993b4be2daa8cdb41e24ca13f6bd945302244e26918f1d081cff0f92c7d328c9c21bba7274fb81fd4ca62d4ada415ffe5d517e17b10729ba479e0

def SM3():
    # 消息体
    data = b'1234'
    # sm3 hash算法，可用于签名消息体
    print(sm3.sm3_hash(func.bytes_to_list(data)))

SM3()

key = "1"

def SM4():
    # 密钥
    print(key)
    # key = b'3l5butlj26hvv313'
    # 消息体
    value = b'111' #  bytes类型
    # 初始化
    crypt_sm4 = sm4.CryptSM4()


SM4()

print(key)