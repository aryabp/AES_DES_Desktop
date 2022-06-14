import sys

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

class Metode_DES:
    def __init__(self,plain,cipher,key,block):
        self.plain = plain
        self.cipher = cipher
        self.key = key
        self.block = int(block)
    def Enkripsi(self):
        try:
            des = DES.new(self.key, DES.MODE_ECB)
            padded_text = pad(self.plain, self.block)
            self.cipher = des.encrypt(padded_text)
        except ValueError:
            self.cipher="Cipher Text Invalid"
        
    def Dekripsi(self):
        des = DES.new(self.key, DES.MODE_ECB)
        self.plain = des.decrypt(self.cipher)
'''
#input plain(unlimited)
key = b"!n1Kunci"
data = b"ini data"
BLOCK_SIZE = 128

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data, BLOCK_SIZE)
encrypt = des.encrypt(padded_text)

#cerak encrypt
print("\n",encrypt,"\n")

#Ini tahapan Deskripsi
key = b'!n1Kunci'
des = DES.new(key, DES.MODE_ECB)
decrypt = des.decrypt(encrypt)

#cetak decrypt
print("\n",decrypt,"\n")
'''