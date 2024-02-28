l=[12,11,66,44,88,18,22,25,32,31,45,76,9,3,8]
print(l)
c1=[]
c2=[]
c3=[]
c4=[]
c5=[]
for i in l:
    if(i<=14):
        c1.append(i)
    if(i>14 and i<=25):
        c2.append(i)
    if(i>25 and i<=40):
        c3.append(i)
    if(i>40 and i<=60):
        c4.append(i)
    if(i>60):
        c5.append(i)
print("14:=",c1)
print("25:=",c2)
print("40:=",c3)
print("60:=",c4)
print("60>:=",c5)
