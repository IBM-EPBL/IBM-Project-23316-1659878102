import random as ra
temp = ra.randrange(0,180)
hum = ra.randrange(0,180)
print("Temperature : ",temp)
print("Humidity : ",hum)
if temp>70:
    if temp>70:
        print("Alarm beep")
elif temp>70:
    if hum<50:
        print("High Temperature Low Humidity")
elif temp<70:
    if hum>50:
        print("High Humidity Low Temperature")
else:
         print("All are good")
