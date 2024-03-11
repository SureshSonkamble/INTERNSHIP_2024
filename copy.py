f=open("abc.txt","r")
data=f.read()

fw=open("D:/VSPI/abc.txt","w")
fw.write(data)
fw.close()
print("file copied Success")
