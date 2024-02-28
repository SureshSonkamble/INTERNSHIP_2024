s1="codingseekho"
s2='codingseekho'
s2='"codingseekho"'
#print(s1)
c=input("Enter character to be search")
cnt=0
for i in s1:
    if(i==c):
        cnt=cnt+1
        
print("Givev Char",c ,"occurs",cnt,"times")
