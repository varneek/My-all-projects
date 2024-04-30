import pywhatkit as open
import pyautogui as auto
from time import sleep
n=0
print("enter 1 to message personal number")
choose=int(input("else enter 2 to message in group:-"))
if choose==1:
    main='+91'
    number=input('enter the number in which you want to spam:-')   
    final=main+number
    time=int(input("enter the number of times you want to send message:-"))
    msg=input("enter the message you want to send:-")
    open.sendwhatmsg_instantly(final,msg)
    while n<time:
        auto.write(msg)
        auto.press("enter")
        sleep(0.2)
        n=n+1
elif choose==2:
    time=int(input("enter the number of times you want to send message:-"))
    msg=input("enter the message you want to send:-")
    print('click on the group in which you want to spam')
    open.sendwhatmsg_to_group_instantly("me",msg)
    while n<time-1:
        auto.write(msg)
        auto.press("enter")
        sleep(0.2)
        n=n+1
else:
    print("invalid command")