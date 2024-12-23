import numpy as np

myarr= np.array([2,3,5,78], np.int32)
print(myarr.dtype)
print(myarr.shape)
myarr[0]=23
print(myarr)

zeroes = np.zeros([2,5])
print(zeroes)

rng =np.arange(10)
print(rng)

lspace = np.linspace(1,5,10)
print(lspace)

emp=np.empty((4,6))
print(emp)

id=np.identity(5)
print(id)

# print(id.reshape(5,1))

print(id.ravel())

x=[[1,2,3],[4,5,6],[7,8,9]]
ar =np.array(x)
print(ar)

print(ar.sum(axis=0))

print(ar.sum(axis=1))

print(ar.T)

print(ar.flat) # Iterator, convert in 1D
for item in ar.flat:
    print(item)

print(ar.size)

print(ar.ndim)

print(ar.nbytes)

#Methods
one = np.array([1,2,5,7,8])
print(one)

print(one.argmax()) # returns index of maximum number

print(one.argmin())

print(one.argsort())

print(np.where(one>5))
