import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import yaml

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

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
        if not iv_generator_phrase == "":
            iv_generator_phrase = key_generator_phrase
    iv = generate_hash(iv_generator_phrase, 16)

    obj2 = AES.new(key, AES.MODE_CFB, iv)
    try:
        psw = obj2.decrypt(ciphertext).decode('utf-8')
    except UnicodeDecodeError as e:
        psw = e

    return psw

def get_configuration():
    conf_path = THIS_DIR + '\\configuration.yml'
    with open(conf_path) as configuration:
        configuration = yaml.safe_load(configuration)
    return configuration

def get_configuration_entries(user='default'):
    configuration = get_configuration()
    path = configuration['output_path'][user]
    columns = configuration['columns']
    name = configuration['name']
    return path, columns, name