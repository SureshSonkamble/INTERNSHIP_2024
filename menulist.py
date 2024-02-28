l=['a','b','c','d']
print(l)
print("1.ADD DATA")
print("2.REMOVE DATA")
print("3.FIND DATA")
print("4.DISPLAY DATA")
print("5.EXIT")
ch=int(input("Enter your choice"))
if(ch==1):
    n=int(input("Enter number of student"))
    for i in range(n):
        nm=input("Entre your name")
        l.append(nm)
        print(l)
if(ch==2):
    l.remove('a')
    print(l)
fnd=0
if(ch==3):
    nm=input("Entre  name to be search")
    for i in l:
        if(i==nm):
           fnd=1
        else:
            fnd=0
if(ch==5):
    exit()
if(fnd==1):
    print("Record Found")
else:
    pass
    #print("No Record Found")
    
