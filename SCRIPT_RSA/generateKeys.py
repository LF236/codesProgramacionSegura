import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def generatePrivateKey():
    privateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend
    )
    return privateKey

def generatePrivateKeyBytes( privateKey ):
    privateKeyBytes = privateKey.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    return privateKeyBytes

def generatePublicKeyBytes( public_key ):
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return public_key_bytes

def savePem( pathPrivateKey, pathPublicKey, privateKey, publicKey ):
    routeI = pathPrivateKey + "private.pem"
    priv = open( routeI, "wb" )
    priv.write( privateKey )
    priv.close()

    routeII = pathPublicKey + "public.pem"
    pub = open( routeII, "wb" )
    pub.write( publicKey )
    pub.close()

if __name__ == "__main__":
    # Verificar que los datos de entrada sean validos
    try:
        rutaPublica = sys.argv[1]
        rutaPrivada = sys.argv[2]

        privateKey = generatePrivateKey()

        # Obtener llave publica de la privada
        publicKey = privateKey.public_key()
        privateKeyBytes = generatePrivateKeyBytes( privateKey )
        publicKeyBytes = generatePublicKeyBytes( publicKey )

        savePem(  rutaPublica, rutaPrivada, privateKeyBytes, publicKeyBytes)

    except IndexError:
        print( 'Error al introducir datos, Seguir la estructura: ' )
        print( '"python generateKeys.py rutaClavePublica rutaClavePrivada"' )
        pass