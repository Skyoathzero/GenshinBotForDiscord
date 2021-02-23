import keyboard
a = True
while 1 : 
    if keyboard.is_pressed('q') == True:
        a = False
    if keyboard.is_pressed('a') == True:
        a = True
    if a == True:
        #do stuff
        print(1)
    else : 
        print(2)