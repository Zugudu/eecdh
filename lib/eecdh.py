from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends.interfaces import PEMSerializationBackend
from cryptography.hazmat.primitives.asymmetric.ec import ECDH

def gen_key(file,o_type='PEM'):
    key=X25519PrivateKey.generate()
    if(file==''):
        file='key'
    if(o_type=='PEM'):
        private=key.private_bytes(Encoding.PEM,PrivateFormat.PKCS8,serialization.NoEncryption())
        pub=key.public_key().public_bytes(Encoding.PEM,PublicFormat.SubjectPublicKeyInfo)
    elif(o_type=='DER'):
        private=key.private_bytes(Encoding.DER,PrivateFormat.PKCS8,serialization.NoEncryption())
        pub=key.public_key().public_bytes(Encoding.DER,PublicFormat.SubjectPublicKeyInfo)
    else:
        print('Invalid output format')
        return
    with open(file,'wb') as fd:
        fd.write(private)
    with open(file+'.pub','wb') as fd:
        fd.write(pub)
    print('Key',file+'[.pub] was generated in',o_type,'format')
def get_ecdh(key,peer_key,type):
    if(key==''):
        key='key'
    if(peer_key==''):
        print('Peer public key doesn\'t specified')
        return
    if(type!='PEM'):
        print('Invalid key format')
        return
    try:
        with open(key,'rb') as fd:
            pkey=load_pem_private_key(fd.read(),None,default_backend())
        with open(peer_key,'rb') as fd:
            pub=load_pem_public_key(fd.read(),default_backend())
        return pkey.exchange(pub)
    except FileNotFoundError as e:
        print(e)
def pure_ecdh(key,peer_key,file,type):
    if(file==''):
        file='shared_key'
    with open(file,'wb') as fd:
        fd.write(get_ecdh(key,peer_key,type))
    print('Shared key was wrote in',file)
def ecdh(key,peer_key,file,type,key_length):
    hkdf=HKDF(hashes.SHA256(),key_length,None,None,default_backend())
    try:
        key=hkdf.derive(get_ecdh(key,peer_key,type))
        with open(file,'wb') as fd:
            fd.write(key)
        print('Shared key was wrote in',file)
    except FileNotFoundError as e:
        print(e)
