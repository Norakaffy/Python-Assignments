import os
Firstname = input(" what's is your first name? ")
lastname = input(" what's is your last name? ")
Gender = input(" what's is your last Gender? ")
YOB= input(" what is your year of birth? ")
PhoneNo = input("what is your Phone Number? ")
os.system("cls")
print("\t\t     Welcome")
FirstName = Firstname.capitalize()
lastName = lastname.capitalize()

print("Fullname: " + FirstName + " " + lastName )
lowercase = FirstName[0] + FirstName[2]+lastName[2]+lastName[3]
uppercase = lowercase.upper()

print ("username: " + uppercase)

# let ab = Firstname[0:5:2] + lastname[1:6:2]

ab = FirstName[0:5:2] + lastName[1:6:2]
passupper = ab.lower()


print ("password: " + passupper)

print ("PhoneNo: " + PhoneNo)
print (PhoneNo.isnumeric())
ghat = "23" * 10 
print(ghat)