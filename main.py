#~~~ Pratham-code ~~~
import random
import os 

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "abcdefghijklmnopqrstuvwxyz"
N = "0123456789"
S = "!@#$%^&*()"

string = A + a + N  

print("~~ password 🗝️ ~~")

length = 10

mpassword = "".join(random.sample(string, length))

os.system('cls')
print ("password-\n" + mpassword)
input("enter for exit\n")

