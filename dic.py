dic={
    'a':101,
    'b':102,
    'c':103,
    'd':104,
    'a':111
    }
print(dic)
#print(dic['a'])
k=[];
v=[];
for i in dic:
    #print(dic[i])
    k.append(i)
    v.append(dic[i])
print("Keys",k)
print("values",v)
