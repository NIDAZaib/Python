```python
#Array
import numpy as np
a =np.arange(6)
a
```




    array([0, 1, 2, 3, 4, 5])




```python
a2 = a[np.newaxis, :]
a2.shape
a2
```




    array([[0, 1, 2, 3, 4, 5]])




```python
#numpy is similar to lists but faster 
list = [3,6,9,12]
list
```




    [3, 6, 9, 12]




```python
print(type(list))
```

    <class 'list'>
    


```python
import numpy as np
a= np.array([5,5,5,5,5,5,])
a
```




    array([5, 5, 5, 5, 5, 5])




```python
type(a)
```




    numpy.ndarray




```python
# 2d array list oflists
b = np.array ([[5,5,5],[5,5,5],[5,5,5]])
b
```




    array([[5, 5, 5],
           [5, 5, 5],
           [5, 5, 5]])




```python
#one dimentional array is also called vector eg line of students
#an array with 2 dimention is matrics eg 10 lines of students
```


```python
#one dimentional array
import numpy as np
a= np.array([5,5,5,])
a
```




    array([5, 5, 5])




```python
type(a)
```




    numpy.ndarray




```python
len(a)
```




    3




```python
a[0]
```




    5




```python
a[0:]
```




    array([5, 5, 5])




```python
# 2d array list oflists
b = np.array ([[5,5,5],[5,5,5],[5,5,5]])
b
```




    array([[5, 5, 5],
           [5, 5, 5],
           [5, 5, 5]])




```python
type(b)
```




    numpy.ndarray




```python
len(b)
```




    3




```python
b[0:]
```




    array([[5, 5, 5],
           [5, 5, 5],
           [5, 5, 5]])




```python
#3d or higher dimention term tensor (used for machine learning and artificial intelegence ) is used .. 
#tensor flow is a library
#j ,k and i operations are used
```


```python
#dimensions are called axis
#first axis has length =2
#second axis has length =3
b = np.array ([[5,5,5],[5,5,5]])
b
```




    array([[5, 5, 5],
           [5, 5, 5]])




```python
#single dimension has one axis
#double dimension has two axis
#3 dimension has 3 axis
```


```python
#how to create an array
import numpy as np
a= np.array([1,2,3,4,5])
a
```




    array([1, 2, 3, 4, 5])




```python
import numpy as np
a= np.zeros(2)
a
```




    array([0., 0.])




```python
c = np.ones(3)
c
```




    array([1., 1., 1.])




```python
#create an empty array with 2 elements 
d= np.empty(3)
d
```




    array([1., 1., 1.])




```python
#with range of elements
e= np.arange (6)
e
```




    array([0, 1, 2, 3, 4, 5])




```python
#with specific range of elemts
f = np.arange(2,20)
f
```




    array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
           19])




```python
#continue
f = np.arange(2,20,2)
f
```




    array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])




```python
#linearly spaced array
h = np.linspace(2,10,num=5) #gives use 5 nums
h
```




    array([ 2.,  4.,  6.,  8., 10.])




```python
#how to create an array for one day
#specific data types in array( if we want only integer array)
i = np.ones(5,dtype=np.int8)
i
```




    array([1, 1, 1, 1, 1], dtype=int8)




```python
j = np.ones(3,dtype=np.float64)
j
```




    array([1., 1., 1.])




```python
#how to create an array 
#2d
np.zeros((3,4)) #3 by 4 axis ka
```




    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])




```python
np.ones((5,6))#5 by 6 axis ka
```




    array([[1., 1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1., 1.]])




```python
np.empty((3,4))#3 by 4 axis ka
```




    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])




```python
#3d array
```


```python
#making and reshaping a 3d array
c = np.arange(24).reshape(2,3,4)
c
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
#day 7 b practice
```


```python
#creating an array using numpy
```


```python
food = np.array(["pakora","samosa","raita"])
food
```




    array(['pakora', 'samosa', 'raita'], dtype='<U6')




```python
price = np.array([5,5,5])
price
```




    array([5, 5, 5])




```python
type(price)
```




    numpy.ndarray




```python
type(food)
```




    numpy.ndarray




```python
len(food)
```




    3




```python
len(food)
```




    3




```python
price[2]
```




    5




```python
price[0:]#if you want to print everything from zero to ownward
```




    array([5, 5, 5])




```python
food[1] #index of array
```




    'samosa'




```python
#dif function of an array
price.mean()

```




    5.0




```python
#zeros
np.zeros(6)
```




    array([0., 0., 0., 0., 0., 0.])




```python
#ones array
np.ones(5)
```




    array([1., 1., 1., 1., 1.])




```python
#empty
np.empty(5)
```




    array([1., 1., 1., 1., 1.])




```python
#range
np.arange(10)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
#specify
np.arange(2-20) #doesnt show anything use comma instead
```




    array([], dtype=int32)




```python
#specify
np.arange(2,20) #doesnt show anything use comma instead
```




    array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
           19])




```python
#same specific range with a specific interval inside this array
np.arange(2,20,2) #things should come with the interval of 2

```




    array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])




```python
#table
np.arange(0,50,5) #actually we have made table of 5 
```




    array([ 0,  5, 10, 15, 20, 25, 30, 35, 40, 45])




```python
#table
np.arange(5,50,5) #actually we have made table of 5.. we can start from 5
```


```python
#table
np.arange(5,55,5) #last digit is exclusive in python
```




    array([ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])




```python
#specific line space
np.linspace(1,100,num=10) #on specific interval show 5 number 
```




    array([  1.,  12.,  23.,  34.,  45.,  56.,  67.,  78.,  89., 100.])




```python
#specific line space
np.linspace(1,100,num=50) #on specific interval show 5 number 
```




    array([  1.        ,   3.02040816,   5.04081633,   7.06122449,
             9.08163265,  11.10204082,  13.12244898,  15.14285714,
            17.16326531,  19.18367347,  21.20408163,  23.2244898 ,
            25.24489796,  27.26530612,  29.28571429,  31.30612245,
            33.32653061,  35.34693878,  37.36734694,  39.3877551 ,
            41.40816327,  43.42857143,  45.44897959,  47.46938776,
            49.48979592,  51.51020408,  53.53061224,  55.55102041,
            57.57142857,  59.59183673,  61.6122449 ,  63.63265306,
            65.65306122,  67.67346939,  69.69387755,  71.71428571,
            73.73469388,  75.75510204,  77.7755102 ,  79.79591837,
            81.81632653,  83.83673469,  85.85714286,  87.87755102,
            89.89795918,  91.91836735,  93.93877551,  95.95918367,
            97.97959184, 100.        ])




```python
#specify your data type
np.ones(5,dtype=np.int64)
```




    array([1, 1, 1, 1, 1], dtype=int64)




```python
#specify your data type
np.ones(50,dtype=np.int64)
```




    array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1], dtype=int64)




```python
#specify your data type
np.ones(50,dtype=np.float64)
```




    array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
           1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
           1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])




```python
#sorting of an array
#array functions
a = np.array([10,12,15,2,4,6,100,332,0.5,10.3]) #int was changed in float
a
```




    array([ 10. ,  12. ,  15. ,   2. ,   4. ,   6. , 100. , 332. ,   0.5,
            10.3])




```python
a.sort()
a
```




    array([  0.5,   2. ,   4. ,   6. ,  10. ,  10.3,  12. ,  15. , 100. ,
           332. ])




```python
#assignment
```


```python

```


```python

```


```python
#concatenate
b = np.array([10.2,3.4,53.6,91.6,45.5])
b
```




    array([10.2,  3.4, 53.6, 91.6, 45.5])




```python
np.concatenate((a,b)) #you can also asort it 
```




    array([  0.5,   2. ,   4. ,   6. ,  10. ,  10.3,  12. ,  15. , 100. ,
           332. ,  10.2,   3.4,  53.6,  91.6,  45.5])




```python
c = np.concatenate((a,b)) #you can also asort it 
c
```




    array([  0.5,   2. ,   4. ,   6. ,  10. ,  10.3,  12. ,  15. , 100. ,
           332. ,  10.2,   3.4,  53.6,  91.6,  45.5])




```python
c.sort()
c
```




    array([  0.5,   2. ,   3.4,   4. ,   6. ,  10. ,  10.2,  10.3,  12. ,
            15. ,  45.5,  53.6,  91.6, 100. , 332. ])




```python
#2d arrays
x = np.array([[1,2],[5,4]])
x
```




    array([[1, 2],
           [5, 4]])




```python
#another 2d arrays
y = np.array([[6,7],[7,8]])
y
```




    array([[6, 7],
           [7, 8]])




```python
#concatenate
c=np.concatenate((x,y), axis=0)
c
```




    array([[1, 2],
           [5, 4],
           [6, 7],
           [7, 8]])




```python
#concatenate
c=np.concatenate((x,y), axis=1)
c
```




    array([[1, 2, 6, 7],
           [5, 4, 7, 8]])




```python
a = np.array([[[0,1,2,3], #for three dimension make 2 dimension this
              [4,5,6,7],
              
             [0,1,2,3],#for three dimension make 2 dimension this
             [5,4,6,7],
              
             [0,1,2,3],
             [5,4,6,7]]])#for three dimension make 2 dimension this
a #we can 3 time single dimension ar 2 dimension
```




    array([[[0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 2, 3],
            [5, 4, 6, 7],
            [0, 1, 2, 3],
            [5, 4, 6, 7]]])




```python
#to find the number of dimensions
a.ndim # 2dimension array k ya one dimension array k 3set comma k bad new chez shuru ho jae pr coma k bd new 
#that make it a tensor array ar 3 dimenstional arra`y
```




    3




```python
#another example
b= np.array([[5,6,7], [8,9,10],
          [10,11,12]])
b 
```




    array([[ 5,  6,  7],
           [ 8,  9, 10],
           [10, 11, 12]])




```python
b.ndim
```




    2




```python
#size of an array or number of elements
a.size
```




    24




```python
#shape of an array or number of elements
a.shape # 1 is dimension and 6 is rows in each dimension also 4 is its column
```




    (1, 6, 4)




```python
a = np.arange(9) #3*3=9
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8])




```python
a.reshape(3,3)#3*3=9
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
np.reshape(a,newshape=(1,9),order ="c")
```




    array([[0, 1, 2, 3, 4, 5, 6, 7, 8]])




```python
#one dimention in to 2 dimension
a = np.array([1,2,3,4,5,6,7,8,9])
a
```




    array([1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
b=a[np.newaxis, :]#row wise 2 dimensional
b
```




    array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])




```python
b.shape
```




    (1, 9)




```python
c=a[: , np.newaxis]
c #c made it column wise 2 dimensional
```




    array([[1],
           [2],
           [3],
           [4],
           [5],
           [6],
           [7],
           [8],
           [9]])




```python
#indexing
a
```




    array([1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
a[2:6]
```




    array([3, 4, 5, 6])




```python
a*6
```




    array([ 6, 12, 18, 24, 30, 36, 42, 48, 54])




```python
a+6
```




    array([ 7,  8,  9, 10, 11, 12, 13, 14, 15])




```python
a.sum()
```




    45




```python
a.mean()

```




    5.0




```python

```


```python

```


```python

```


```python

```


```python

```
