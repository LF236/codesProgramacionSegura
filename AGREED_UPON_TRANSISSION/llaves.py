from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Generar llave privada
def generar_privada():
    private_key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = 2048,
        backend = default_backend
    )
    return private_key

# Generar llave publica desde la llave privada
def generar_publica( llave ):
    return llave.public_key()

# Convertir llave privada a bytes sin cifrar los bytes, a partir del resultado se puede guardar un archivo binario
def convertir_llave_privada_bytes( llave ):
    private_key_bytes = llave.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
    )
    return private_key_bytes

# Convertir llave publica a bytes
def convertir_llave_publica_bytes( llave ):
    public_key_bytes = llave.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_key_bytes

# Convertir llave privada de bytes a objeto llave, como los bytes no estan cifrados no se require de una llave
def convertir_bytes_llave_privada( binario ):
    private_key = serialization.load_der_private_key(
        binario,
        backend = default_backend(),
        password = none
    )
    return private_key

# Convertir la llave publica de bytes a objeto llave
def convertir_bytes_llave_publica(binario):
    public_key = serialization.load_der_public_key(
        binario,
        backend = default_backend()
    )
    return public_key

# Funciones para interacuar con archivos
def guardar_binario(ruta, binario):
    with open(ruta, 'bw') as archivo:
        archivo.write(binario)

        
def recuperar_publica_from_path(path):
    with open(path, 'rb') as archivo:
        binario = archivo.read()
    return convertir_bytes_llave_publica(binario)


def recuperar_privada_from_path(path):
    with open(path, 'rb') as archivo:
        binario = archivo.read()
    return convertir_bytes_llave_privada(binario)

if __name__ == '__main__':
    llave_privada = generar_privada()
    llave_publica = generar_publica( llave_privada )
    privada_binario = convertir_llave_privada_bytes( llave_privada )
    publica_binario = convertir_llave_publica_bytes( llave_publica )
    guardar_binario( 'publica.pem', publica_binario )
    guardar_binario( 'privada.pem', privada_binario )