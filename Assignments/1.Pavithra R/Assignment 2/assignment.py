import random as a
temp = a.randint(50,100)
hum = a.randint(150,300)
print(temp,hum)
if temp>80:
    if hum>80:
        print("hazard")

    else:
        print("high temperature")
elif temp==80:
     print("normal temperature")
else:
    print("all good")
