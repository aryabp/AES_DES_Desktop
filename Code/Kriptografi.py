from Setup input Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

'''
from DES import Metode_DES as DES

Kelas_DES = DES(b"ini data","",b"!n1Kunci",16)
Kelas_DES.Enkripsi()
print(Kelas_DES.cipher)

Kelas_DES = DES("",b'I\xc0\xa1\x9dc6\xa5\xaf5\x07_h\x1b\xcc\xdc\x9a',b"!n1Kunci","")
Kelas_DES.Dekripsi()
print(Kelas_DES.plain)
'''

from AES import Metode_AES as AES

# input plain(unlimit),key(16digitbyte)
# output cipher,tag,nonce

Kelas_AES = AES(bytes('ini data yang akan dilakukan AES','utf-8'),"",bytes('1!nikuncIyangpas','utf-8'),"","")
Kelas_AES.Enkripsi()
print("\n",Kelas_AES.cipher,"\n",Kelas_AES.tag,"\n",Kelas_AES.nonce,"\n")

#input cipher,key,tag,nonce
#output plain

Kelas_AES = AES("",b'\xc0\x103\x07\x0b\xb2Vl\x96J\xbc\x18\xb7by\xb4\x00\xea\xdd\xd5\x02#X)N\\\xc4\xa5\x94tq\xc4',b'1!nikuncIyangpas',b'\xfc]\x99\x1f0\x13\x8e)t\x8114\x85Y,N',b' e\xc2\xa2h\xc2&\x9d\x88\x97M\x13Z\x95\xfe\xe6')
Kelas_AES.Dekripsi()
print(Kelas_AES.plain)
