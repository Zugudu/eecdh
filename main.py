#!/usr/bin/python3
import eecdh
import menu

if __name__=='__main__':
    try:
        while True:
            com=input('>')
            if(com=='exit'):
                exit(0)
            elif(com=='gen'):
                eecdh.gen_key()
                print('Public and private keys was generated')
            elif(com=='t'):
                print(menu.menu('What is 42?',('42','15','apple','for est')))
            else:
                print('Unknown command!\ngen\t-\tgenerate keys')
    except EOFError:
        print()
