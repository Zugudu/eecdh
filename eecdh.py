from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

def gen_key(file='key',o_type='PEM'):
    key=X25519PrivateKey.generate()

    if(o_type=='PEM'):
        private=key.private_bytes(Encoding.PEM,PrivateFormat.PKCS8,serialization.NoEncryption())
        pub=key.public_key().public_bytes(Encoding.PEM,PublicFormat.SubjectPublicKeyInfo)
    else:
        private=key.private_bytes(Encoding.DER,Encoding.PKCS8,serialization.NoEncryption())
        pub=key.public_key().public_bytes(Encoding.DER,PublicFormat.SubjectPublicKeyInfo)
    with open(file,'wb') as fd:
        fd.write(private)
    with open(file+'.pub','wb') as fd:
        fd.write(pub)