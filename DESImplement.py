import os
from Crypto.Cipher import DES3
from Crypto import Random

class DESImplement:

    def generateKey():
        #16 byte key
        key = ''.join(chr(random.randint(0, 0xFF)) for i in range(8))
        fd = open("DES_key.pem", "wb")
        fd.write(AES_key)
        fd.close()
        return key

################################################################################
    def encrypt_file(in_filename, out_filename, chunk_size, key):
        iv = Random.get_random_bytes(8)
        des3 = DES3.new(key, DES3.MODE_CFB, iv)
        with open(in_filename, 'r') as in_file:
            with open(out_filename, 'w') as out_file:
                while True:
                    chunk = in_file.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)
                    out_file.write(des3.encrypt(chunk))

################################################################################################
def decrypt_file(in_filename, out_filename, chunk_size, key, iv):
    des3 = DES3.new(key, DES3.MODE_CFB, iv)
    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                out_file.write(des3.decrypt(chunk))
