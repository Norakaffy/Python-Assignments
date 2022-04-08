

import os
print("\t\t\tRegistration")
print("========================================")

Firstname = input(" what's is your first name? ")
lastname = input(" what's is your last name? ")
Gender = input(" what's is your last Gender? ")
YOB= input(" what is your year of birth? ")
os.system("cls")

print("========================================")

print("Fullname: ", Firstname +" "+ lastname)
print("username: ", Firstname[0]+Firstname[1] + lastname[2]+ lastname[3])
# print("password: ", Firstname[0]+Firstname[2]+Firstname[4] + lastname[1]+lastname[3]+lastname[5] )
print("password:", Firstname[0:5:2] + lastname[1:6:2])
print("YOB: ",YOB )
xy=int(YOB)
gb= 2021
age= gb-xy
print("age: ", age)



os.system("cls")

print("\t\t     Welcome")

print("Fullname: " + Firstname + " " + lastname )
lowercase = Firstname[0] + Firstname[2]+lastname[2]+lastname[3]
uppercase = lowercase.upper()
print ("username: " + uppercase)

# let ab = Firstname[0:5:2] + lastname[1:6:2]

ab = Firstname[0:5:2] + lastname[1:6:2]
passupper = ab.lower()
print ("password: " + passupper)


