l=[12,11,66,44,88,18,22,25,32,31,45,76,9,3,8]
print(l)
c1=0
c2=0
c3=0
c4=0
c5=0
for i in l:
    if(i<=14):
        c1=c1+1
    if(i>14 and i<=25):
        c2=c2+1
    if(i>25 and i<=40):
        c3=c3+1
    if(i>40 and i<=60):
        c4=c4+1
    if(i>60):
        c5=c5+1  
print("14:=",c1)
print("25:=",c2)
print("40:=",c3)
print("60:=",c4)
print("60>:=",c5)
