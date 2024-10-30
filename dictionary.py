# dictionary

'''d1={1:"A",2:"B"}
print(d1[2]) #B o/p
#print(d1["B"]) #key error

print(d1)

print(d1.key)

for key in d1.keys():
    print(key)

for value in d1.values():
    print(key)

for key,value in d1.items():
    print(key,[" ",value])

d1={1:"A",2:"B"}
print(d1.get(7,4))
'''

customer_detail={1001:"john",1004:"jill",1005:"joe",1003:"jack"}

#a
print(customer_detail)

#b
print(len(customer_detail))

#c
for v in sorted(customer_detail.values()):
    print(v)
    
#d
del customer_detail[1005]
print(customer_detail)

#e
#updation
customer_detail[1003]="Marry"
print(customer_detail)

#f
if 1002 in customer_detail:
    print("yes it is available")

else:
    print("yes it is not available")





