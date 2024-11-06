p='for'
s='abforxxrfoyyroforxx'
n=len(s)
d={}
for i in p:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
print(len(d))
   
