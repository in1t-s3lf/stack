!# /usr/bin/env python3

stack=[]
ext=False
while(ext==False):
    cmd=input()
    if(cmd[:4]=='push'):
        stack.append(cmd[5:])
        print('ok')
    elif(cmd=='pop'):
        print(stack.pop())
    elif(cmd=='back'):
        print(stack[len(stack)-1])
    elif(cmd=='size'):
        print(len(stack))
    elif(cmd=='clear'):
        stack.clear()
        print('ok')
    elif(cmd=='exit'):
        print('bye')
        ext=True
