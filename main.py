#!/usr/bin/python3
from lib import eecdh
from sys import argv

if __name__=='__main__':
    action=0
    o_type='PEM'
    name=''
    peer_pub=''
    key=''
    length=32
    #0-help
    #1-gen
    #2-ECDH with HKDF
    #3-Pure ECDH
    for i in range(1,len(argv)):
        if(argv[i][0]=='-'):
            if(argv[i]=='-h'):
                pass
            elif(argv[i]=='-g'):
                action=1
            elif(argv[i]=='-n'):
                name=argv[i+1]
            elif(argv[i]=='-t'):
                o_type=argv[i+1]
            elif(argv[i]=='-i'):
                peer_pub=argv[i+1]
            elif(argv[i]=='-k'):
                key=argv[i+1]
            elif(argv[i]=='-dh'):
                action=2
            elif(argv[i]=='-pdh'):
                action=3
            elif(argv[i]=='-l'):
                length=int(argv[i+1])
        else:
            pass
    if(action==0):
        print(
'Invalid command\n\
-dh [-k -i -n -t -l] — computate shared key with ECDH+HKDF and save to *share_key*\n\
-pdh [-k -i -n -t] — computate shared key with pure ECDH and save to *share_key*\n\
-g\t\t— generate key\'s pair and save it DEFAULT=key[.pub]\n\
-h\t\t— help page\n\
-t [PEM|DER]\t— set output/imported key type DEFAULT=PEM\n\
-n name\t\t— set output file name\n\
-i peer_key\t— import peer public key from peer_key\n\
-k key\t\t— import private key DEFAULT=key\n\
-l key_length\t— set key length in bytes for KDF DEFAULT=32')
    elif(action==1):
        print('Key generation...')
        eecdh.gen_key(file=name,o_type=o_type)
    elif(action==2):
        eecdh.ecdh(key,peer_pub,name,o_type,length)
    elif(action==3):
        eecdh.pure_ecdh(key,peer_pub,name,o_type)
