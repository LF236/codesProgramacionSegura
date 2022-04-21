import sys
import os
import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
import padding
import llaves
MENSAJE = b'Hello World'

def conectar_servidor( host, puerto ):
    # Creación del cliente TCP
    cliente = socket.socket (socket.AF_INET, socket.SOCK_STREAM )
    try:
        cliente.connect( ( host, int( puerto ) ) )
        return cliente
    except:
        print( 'Servidor inalcanzable' )
        exit()

def generar_llaves():
    aes = os.urandom( 16 )
    iv = os.urandom( 16 )
    mac = os.urandom( 128 )
    return aes, iv, mac

def firmar_llaves( aes, iv, mac, llave_privada ):
    mensaje = aes + iv + mac
    signature = llave_privada.sing(
        mensaje,
        padding.PSS(
            mgf = padding.MG
        )
    )
    pass

def proteger_mensaje( mensaje = MENSAJE ):
    aes, iv, mac = generar_llaves()
    # Firma digital sobre la concatenacion de las llaves

if __name__ == '__main__':
    socket = conectar_servidor( sys.argv[ 1 ], sys.argv[ 2 ] )
    # Ruta de la llave pública en formato PEM
    llave_publica_path = sys.argv[ 3 ]
    llave_publica = llaves.recuperar_publica_from_path( llave_publica_path )
   
    # print( 'Hola zorra' )

# 1.13