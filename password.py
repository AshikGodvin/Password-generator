import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol = "=-*()@$%!"
all=lower+upper+number+symbol
length=int(input("enter the length for your password: "))
password="".join(random.sample(all,length))
print("the password you generated is :", password)
print("copy your password")
