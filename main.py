#!/usr/bin/python3
import eecdh
import menu
from sys import argv

if __name__=='__main__':
    action=0
    o_type='PEM'
    name=''
    #0-help
    #1-gen
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
        else:
            pass
    if(action==0):
        print(
'Invalid command\n\
-dh public_key\t— computate sahred key with EECDH and save to *share_key*\n\
-g\t\t— generate key\'s pair and save it\n\
-h\t\t— help page\n\
-t [PEM|DER]\t\t— set output key type\n\
-n name\t\t— set output file name')
    elif(action==1):
        print('Key generation...')
        eecdh.gen_key(file=name,o_type=o_type)
