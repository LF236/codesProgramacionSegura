from email.mime import base
import os
import sys
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Mensajes

def mensajesCbc( key = "", iv = "" ):
    # Pasar la clave y el iv a base 64
    key = key.encode( 'ascii' )
    keyBase64 = base64.b64encode( key )

    iv = iv.encode( 'ascii' )
    ivBase64 = base64.b64encode( iv )

    print( len(keyBase64) )
    print( len(ivBase64) )
    # Proceso de cifrado
    aesCipher = Cipher( algorithms.AES( keyBase64 ), modes.CBC( ivBase64 ), backend = default_backend )
    print( aesCipher )
    pass
if __name__ == '__main__':
    key = sys.argv[ 1 ]
    iv = sys.argv[ 2 ]
    mensajesCbc( key, iv )
