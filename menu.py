def menu(question,case):
    while True:
        cx=0
        print(question)
        for i in case:
            print(chr(ord('a')+cx)+')'+i)
            cx+=1
        ans=ord(input('>')[0])-ord('a')
        if(ans>=0 and ans<len(case)):
            return ans
        else:
            print('Invalid input!')
