import hashlib


# MD5加密
def MD5(x):
    hash_md5 = hashlib.md5()
    hash_md5.update(x.encode('utf-8'))
    return hash_md5.hexdigest()