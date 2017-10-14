import msvcrt as ms

key = ms.getwch()
print(key)
oldkey = key

while True:
    key = ms.getwch()
    #if(oldkey != key):
    #    print(ord(key))
        
    if(key == 'q'):
        break
    elif(ord(key) == 72):
        print("UP");
    elif(ord(key) == 80):
        print("DOWN");
    elif(ord(key) == 75):
        print("LEFT");
    elif(ord(key) == 77):
        print("RIGHT");
    
