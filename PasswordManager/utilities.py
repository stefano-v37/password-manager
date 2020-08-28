from Crypto.Cipher import AES
from Crypto.Hash import SHA256


def generate_hash(generator_str, bits):
    if (bits <= 32) & (bits > 0) & (type(bits) is int):
        hash = SHA256.new(data=bytes(generator_str, 'utf-8')).digest()[0:bits]
    return hash

def crypt(psw, key_generator_phrase, iv_generator_phrase=None):
    key = generate_hash(key_generator_phrase, 32)
    if not iv_generator_phrase:
        iv_generator_phrase = key_generator_phrase
    iv = generate_hash(iv_generator_phrase, 16)

    obj = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = obj.encrypt(psw)
    psw_crypted = ciphertext

    return psw_crypted

def uncrypt(psw_crypted, key_generator_phrase, iv_generator_phrase=None):
    ciphertext = psw_crypted
    key = generate_hash(key_generator_phrase, 32)
    if not iv_generator_phrase:
        iv_generator_phrase = key_generator_phrase
    iv = generate_hash(iv_generator_phrase, 16)

    obj2 = AES.new(key, AES.MODE_CFB, iv)
    psw = obj2.decrypt(ciphertext).decode('utf-8')

    return psw