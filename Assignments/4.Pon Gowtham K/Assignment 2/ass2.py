import random as ra
temp = ra.randrange(0,180)
hum = ra.randrange(0,180)
print("Temperature : ",temp)
print("Humidity : ",hum)
if temp>90:
    if temp>90:
        print("Alarm beep")
elif temp>90:
    if hum<90:
        print("High Temperature Low Humidity")
elif temp<90:
    if hum>90:
        print("High Humidity Low Temperature")
else:
         print("All are good")
