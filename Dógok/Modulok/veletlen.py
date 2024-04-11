from random import random

#Generáljunk egy random számot!

print("[0, 1[: ",random())

print("[0, 15[: ",random()*15)

#[0..5] = {0, 1, 2, 3, 4, 5}
#for i in range(400):
r = random() * 6
print("[0..5]: ", int(r))

#Dobókocka: [1..6]
r = random() * 6
print("Kocka: ",int(r)+1)

#[13..19] => {13, 14, 15, 16, 17, 18, 19}
r = int(random()*7)+13
print("[13..19]: ", r)


#Általában:
#[a..b]
#hossz = b-a+1
#kezdo = a
#r = int(random()* (b - a + 1)) + a