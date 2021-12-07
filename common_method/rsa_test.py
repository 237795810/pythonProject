import rsa

"""使用rsa生成加密和解密的密钥"""
def create_keys():
    (pubkey, privkey) = rsa.newkeys(256)
    pub = pubkey.save_pkcs1()
    with open("public1.pem", "wb+") as f:
        f.write(pub)

    pri = privkey.save_pkcs1()
    with open("private1.pem","wb+") as f:
        f.write(pri)

# if __name__ == '__main__':
#     create_keys()

# def encrypt():
    with open("public1.pem","rb") as key:
        key1 = key.read()

    pubkey = rsa.PublicKey.load_pkcs1(key1)
    ras_a = "casun36689".encode("utf-8")
    ras_a_text = rsa.encrypt(ras_a,pubkey)
    print(ras_a_text.decode("utf-8","ignore"))

    with open("private.pem", "rb"):
        pass

