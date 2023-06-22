#Bài 1
conversion = [(1),(0.000043),(0.000063),(0.0060),(0.000033),(0.000039),(0.000038),(0.0015)]
currency = int(input("1. VND to different currency\n2. Different currency to VND"))
if currency == 1:
    money = int(input("vietnamese currency: "))
    print("0. VND","1. USD","2. AUD","3. Yen","4. Pounds","5. Euros","6. Franc","7. Baht",sep = "\n")
    convert = int(input("Choose currency to convert to: "))
    money = money * conversion[convert]    
elif currency == 2:
    money = int(input("Amount of money: "))
    print("0. VND","1. USD","2. AUD","3. Yen","4. Pounds","5. Euros","6. Franc","7. Baht",sep = "\n")
    convert = int(input("Currency you are converting: "))
    money = money / conversion[convert]
print(money)

#Bài 2
pi = 3.14
r = 0
perim = 2*r*pi
area = pi*(r^2)
r = int(input("Radius of circle: "))
print("Perimeter: ",perim,"\nArea: ",area)

#Bài 3
for i in range(3):
    time = int(input("Time of athelete ",i," (in seconds)"))
    total = total + time
average = total / i
print (average)