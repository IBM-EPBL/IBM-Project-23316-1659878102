import random as ran

temp = ran.randrange(0,180)#temperature
hum = ran.randrange(0,180)#humidity
print("Temperature : ",temp)
print("Humidity : ",hum)
if temp>90:
    if hum>90:
        print("Alarm Beep!")
elif temp>90 and hum<90:
    print("High Temperature Low Humidity")
elif temp<90 and hum>90:
    print("High Humidity Low Temperature")
else:
    print("Temperature And Humidity are Good")
