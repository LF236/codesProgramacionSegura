import sys
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


def publicBytesToKey(publicKeyBytes):
    publicKey = serialization.load_pem_public_key(
        publicKeyBytes,
        backend=default_backend()
    )

    return publicKey


def privateBytesToKey(privateKeyBytes):
    privateKey = serialization.load_pem_private_key(
        privateKeyBytes,
        backend=default_backend(),
        password=None
    )

    return privateKey


def simple_rsa_encrypt(m, publickey):
    ciphertext1 = publickey.encrypt(
        m,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))  # se usa rara vez dejar None
    return ciphertext1


def simple_rsa_decrypt(c, privatekey):
    recovered1 = privatekey.decrypt(
        c,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
    return recovered1


if __name__ == "__main__":
    try:
        operation = sys.argv[1]
        fileInput = sys.argv[2]
        fileOutput = sys.argv[3]
        routeKey = sys.argv[4]

        fileI = open(fileInput, "rb")
        text = fileI.read()
        fileI.close()

        fileII = open(routeKey, "rb")
        key = fileII.read()
        fileII.close()

        arrKey = key.decode('utf-8').split('-')
        if arrKey[5] == "BEGIN RSA PRIVATE KEY":
            key = publicBytesToKey(key)
        else:
            key = privateBytesToKey(key)
        
        if operation == "cifrar":
            code = simple_rsa_encrypt( text, key )
            fileTemp = open( fileOutput, "wb" )
            fileTemp.write( code )
            fileTemp.close()
        else:
            code = simple_rsa_decrypt( text, key )
            fileTemp = open( fileOutput, "wb" )
            fileTemp.write( code )
            fileTemp.close()

    except IndexError:
        print('Error al introducir datos, Seguir la estructura: ')
        print('"python operation.py cifrar/descifrar archivoEntrada archivoSalida rutaLlave"')
        pass
