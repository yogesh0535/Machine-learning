import numpy as np
'''
# array from list
listarray=np.array([[1,3,2],[4,5,6],[7,8,9]])
print(listarray)
print(listarray.size)


# array from dictionary
dictarr=np.array({1,2,3})
print(dictarr)

# zeroes array
zeroes=np.zeros((2,4))              #zero matrix of 2 row and 4 colomn 
print(zeroes)


# arrange function
rng=np.arange(13)               # printing numbers to 13
print(rng)

# linespace function  ==>> creates equal spacebetween two numbers
lspace=np.linspace(1,5,12)      # creates 12 equal spaces between 1 and 5 
lspace=np.linspace(1,4,8)      # creates 8 equal spaces between 1 and 4 
print(lspace)


# empty function ==>> creates an empty matrix that have garbage numbers
emp=np.empty((1,3))
emp1=np.empty((3,2))
print(emp)
print(emp1)

# identity matrix 
id=np.identity(4)
print(id)
print(id.shape)


# ravel module ==>> changes multi dimensional array to 1-d array or flatter array
array=np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2]])
print(array)
print(array.ravel())


#reshape of matrix
arr=np.arange(20)
print(arr)
print(arr.reshape(4,5))               # as 4*5 = 20


arr1=np.array([1,23,45,456,64,34,24,60]).reshape(2,4)
print(arr1)
print(len(arr1))
print(arr1.shape)
'''

'''
# range function 
n=int(input("enter the value: "))
arr=np.array([range(1,n)]).reshape(3,3)
print(arr)

# arange function
print(list(range(10,15)))

a1=np.arange(10,15)         #start=10   end=15   step=1
print(a1)

a2=np.arange(10,50,6)               #start=10  end= 50  step=6
print(a2)

a3=np.arange(10, 3,-1)              # start=10   end=3   step=-1
print(a3)
'''

r=np.array([10,20,30,40,50,60,70,80,90])








