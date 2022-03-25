"""
    No se necesita usar un padding, por lo que se pueden procesar datos planos
    de cualquier tamaño sin preocuparnos C:
    Notas:
        -finaliza() ya no se hace nada pero es buena practica seguir usandolo.
"""
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = os.urandom( 16 )
iv = os.urandom( 16 )

aesCipher = Cipher( algorithms.AES( key ), modes.CTR( iv ), backend = default_backend )
aesEncryptor = aesCipher.encryptor()

datos = b'lf236' # Datos que no soy de 16bytes

cifrado = aesEncryptor.update( datos )
aesEncryptor.finalize()
print( cifrado )

aesDecryptor = aesCipher.decryptor()

plano = aesDecryptor.update( cifrado )
aesDecryptor.finalize()
print( plano )