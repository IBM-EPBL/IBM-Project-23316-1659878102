import random as a
temp = a.randint(50,100)
print('Temperature=',temp)
hum = a.randint(150,300)
print('Humidity=',hum)
if temp>80:
    print("Hazardous condition")
else:
    print("Normal condition")
