import random
nn = random.randint(0, 1)
#print(nn)
n=int(input("Enter number to guess"))
if(n==nn):
    print("Right")
else:
    print("Wrrong")
print(nn)
