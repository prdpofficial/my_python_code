import numpy as np

list1=[[1,2,3,4,5,100],
       [6,7,8,9,10,200],
       [11,12,13,14,15,300]]
arr1= np.array(list1, dtype='int')
#arr2= arr1.astype("int").astype('str')
print(type(arr1))

#changing shape of array
    #finding the shape of array
print('Shape of array is: ',arr1.shape)

    #finding the data type of array
print('data type of array is: ' ,arr1.dtype)

    #finding the size of array
print('size of array is: ', arr1.size)

    #finding dimensions of array like 1d,2d,3d
print('Num dinmensions of array is: ',arr1.ndim)

#how to extract specific item from an array
#extract the first 2 rows and columns
print('extracted first 2 rows & columns : ',arr1[:2, :2])

#find mean , max and min on ndarray(numpyarray)
print("mean value is: ",arr1.mean())
print("max value is: ",arr1.max())
print("min value is: ",arr1.min())

# Row wise and column wise min
print("Column wise minimum: ", np.amin(arr1, axis=0))
print("Row wise minimum: ", np.amin(arr1, axis=1))

#copy array
#method1 this is not copy if we change in copy it wil reflect in orignal also
arr2= arr1[:2,:3]
#arr2[:1,:1]=25  it will change the arr1 also replace 1 with 25

#method2 this will do proper copy of array
arr3 = arr1[:2,:3].copy()
#arr3[:1,:1] =25 will not redlect in arr1 so its pure copy

#REShaping array
print(arr1.reshape(6,3))

#flatten array change into 1 d
print(arr1.flatten())

a=arr1.flatten()
count=0
for i in a:
    count+=i
print(count)

#3d reshape
print(arr1.reshape(3,2,3))


