s1=int(input("Enter sub1 marks"))
s2=int(input("Enter sub2 marks"))
s3=int(input("Enter sub3 marks"))
ttl=s1+s2+s3
per=ttl/3

print(ttl)
p=int(per)
print(p,"%")
if(p>=75):
    print("A+")
elif(p<75 and p>=60):
    print("A")
elif(p<60 and p>=50):
    print("B")
else:
    print("fail")
