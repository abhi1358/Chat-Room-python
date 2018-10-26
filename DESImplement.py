import os
from Crypto.Cipher import DES3
from Crypto import Random
import numpy as np
import sys, struct

class DESImplement:

    def generateKey(self):
        #16 byte key
        DES_key = ''.join(chr(np.random.randint(0, 100)) for i in range(16))
        fd = open("DES_key.pem", "wb")
        fd.write(bytes(str.encode(DES_key,"utf-8")))
        self.iv = Random.get_random_bytes(8)
        fd.close()
        return DES_key

################################################################################
    def encrypt_file(self,in_filename, out_filename, chunk_size=8192, key):
       # iv = Random.get_random_bytes(8)
        des3 = DES3.new(key, DES3.MODE_CFB, self.iv)
        with open(in_filename, 'rb') as in_file:
            with open(out_filename, 'wb') as out_file:
                while True:
                    chunk = in_file.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    out_file.write(des3.encrypt(chunk))

################################################################################################
    def decrypt_file(self,in_filename, out_filename, chunk_size=8192, key):
       # iv = Random.get_random_bytes(8)
        des3 = DES3.new(key, DES3.MODE_CFB, self.iv)
        with open(in_filename, 'rb') as in_file:
            with open(out_filename, 'wb') as out_file:
                while True:
                    chunk = in_file.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    out_file.write(des3.decrypt(chunk))

