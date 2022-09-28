import random as r

temp=r.randrange(0,180)
humidity=r.randrange(0,100)
print(temp)
print(humidity)
if temp>80:
    if humidity >80:
        print("Alarm beep")
elif temp==80:
    print("High temp")
else:
    print("All good")
