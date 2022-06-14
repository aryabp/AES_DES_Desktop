from Crypto.Cipher import AES

class Metode_AES:
    def __init__(self,plain,cipher,key,tag,nonce):
        self.plain = plain
        self.cipher = cipher
        self.key = key
        self.tag = tag
        self.nonce = nonce

    def Enkripsi(self):
        chiper = AES.new(self.key, AES.MODE_EAX)
        self.nonce = chiper.nonce
        self.cipher, self.tag = chiper.encrypt_and_digest(self.plain)
        #Akses output self.cipher, self.tag, self.nonce
    def Dekripsi(self):
        chiper = AES.new(self.key, AES.MODE_EAX, self.nonce)
        self.plain = chiper.decrypt(self.cipher)
        try:
            chiper.verify(self.tag)
        except ValueError:
            self.plain=b'kuncinya sepertinya ada yang salah'
        #Akses output self.plain
'''
data = b'ini data yang akan dilakukan AES'
key = b'1!nikuncIyangpas' #16 bit untuk AES

chiper = AES.new(key, AES.MODE_EAX)
nonce = chiper.nonce
chiperText, tag = chiper.encrypt_and_digest(data)

print(chiperText,'\n',tag,'\n',nonce,'\n')

#dekripsi
key = b'1!nikuncIyangpas' #16 bit untuk aes
chiper = AES.new(key, AES.MODE_EAX, nonce)
plaintext = chiper.decrypt(chiperText)
try:
    chiper.verify(tag)
    print(plaintext.decode())
except ValueError:
    print("kuncinya sepertinya ada yang salah")
'''