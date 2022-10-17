import random as r

temp=r.randrange(0,180)
humidity=r.randrange(0,100)
print(temp)
print(humidity)
if temp>80 and humidity >80:
        print("Alarm beep")
elif temp>80 and humidity<80:
    print("High temp and low humidity")
elif temp <80 and humidity>80:
    print("Low temp and high humidity")
else:
    print("All good")
