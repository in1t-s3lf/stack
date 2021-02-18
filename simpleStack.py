!# /usr/bin/env python3

stack=[]
ext=False
while(ext==False):
    cmd=input()
    if(cmd[:4]=='push'):
        stack.append(cmd[5:])
        print('ok')
    elif(cmd=='pop' or cmd=='back'):
        if(len(stack)>=1 and cmd=='pop'):
            print(stack.pop())
        elif(len(stack)>=1 and cmd=='back'):
            print(stack[len(stack)-1])
        else: print('error')
    elif(cmd=='size'):
        print(len(stack))
    elif(cmd=='clear'):
        stack.clear()
        print('ok')
    elif(cmd=='exit'):
        print('bye')
        ext=True
