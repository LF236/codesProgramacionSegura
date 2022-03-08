from ast import Not
import base64
from pydoc import describe
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
def verificarEntradas16Bytes( cadena64 ):
    if len( cadena64 ) == 16:
        return True
    else:
        return False

def validarEntradaOperacion( operacion ):
    if operacion == 'cifrar' or operacion == 'descifrar':
        return True
    else:
        return False

def cifrar( archivoEntrada, archivoSalida, clave, iv ):
    aesCipher = Cipher( algorithms.AES( clave ), modes.CTR( iv ), backend = default_backend )
    aesEncryptor = aesCipher.encryptor()
    salida = open( archivoSalida, 'wb' )

    for buffer in open( archivoEntrada, 'rb' ):
        cifrado = aesEncryptor.update( buffer )
        salida.write( cifrado )
    aesEncryptor.finalize()
    salida.close()

def descifrar( archivoEntrada, archivoSalida, clave, iv ):
    aesCipher = Cipher( algorithms.AES( clave ), modes.CTR( iv ), backend = default_backend )
    aesDecryptor = aesCipher.encryptor()
    salida = open( archivoSalida, 'wb' )
    textoPlano = b''
    for buffer in open( archivoEntrada, 'rb' ):
        textoPlano = aesDecryptor.update( buffer )
        salida.write( textoPlano )

    aesDecryptor.finalize()
    salida.close()

if __name__ == "__main__":
    # Archivo de entrada, archivo de salida, llave, IV
    try:
        # Obtenemos los valores de entrada
        archivoEntrada = sys.argv[ 1 ]
        archivoSalida = sys.argv[ 2 ]
        clave = sys.argv[ 3 ]
        iv = sys.argv[ 4 ]
        operacion = sys.argv[ 5 ]
        
        # Validamos que la operación sea cifrar o descifrar
        if not validarEntradaOperacion( operacion ):
            print( '\nLa operación solo puede ser "cifrar" o "descifrar"' )
            exit()

        # Cambiamos la llave y el IV a base64
        clave = clave.encode( 'ascii' )
        clave64 = base64.b64encode( clave )

        iv = iv.encode( 'ascii' )
        iv64 = base64.b64encode( iv )

        # Verificamos que la llave y el IV sean de 16 bytes
        if not verificarEntradas16Bytes( clave64 ):
            print( 'La llave debe ser de 16 bytes ' )
            exit()
        if not verificarEntradas16Bytes( iv64 ):
            print( 'El iv debe tener 16 bytes' )
            exit()

        # Validar que operación se va a realizar y disparar el método correspondiente
        if operacion == 'cifrar':
            print( 'Proceso para cifrar' )
            cifrar( archivoEntrada, archivoSalida, clave64, iv64 )
        
        if operacion == 'descifrar':
            print( 'Proceso para descifrar' )
            descifrar( archivoEntrada, archivoSalida, clave64, iv64 )
    except IndexError:
        print( 'Error al introducir datos, Seguir la estructura: ' )
        print( '"python code.py archivoEntrada archivoSalida clave IV cifrar/descifrar"' )
        pass

    