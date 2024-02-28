pwd=input("Enter password")
l=len(pwd)
uc=0
lc=0
dg=0
for i in pwd:
    if(i.isdigit()):
        dg=1
    if(i.isupper()):
        uc=1    
    if(i.islower()):
        lc=1
if(uc==1 and lc==1 and dg==1 and l>=8):
    print("Valid Password")
else:
    print("Invalid Password")
