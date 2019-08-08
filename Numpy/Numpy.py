#!/usr/bin/env python
# coding: utf-8

# ## Numpy Tutorial
# **Author - Abhijeet Bhilare** \
# **github link - https://github.com/abhijeet-bhilare-1990/Python**\
# **reference - https://docs.scipy.org/doc/numpy/reference/**
# 
# ### Basics of Numpy
# Numpy is library used for scintific and mathematical computation of data.It is mostly used for\
# **1. Numerical analysis**\
# **2. Matrix Computation (Multi D)**\
# **3. Linear Algebra**\
# Numpy is used as array in Python as python does not support inbuild array container but list.\
# List are expensive in terms of performance for insert, search operations, to overcome this Numpy was introduced.
# 
# In python3 you can install Numpy using below command \
# **pip3 install numpy** \
# make sure you dont have any proxy, if proxy is there please penetrate proxy using following command \
# **pip3 --proxy https://username:password@proxyname:portnumber install numpy** 
# 
# ### Limitations
# 1. This tutorial is very basic and covers only basic functions of Numpy
# 
# ### Future Learnings
# 1. Explore Linear Algebra more deeply - eg. how to solve linear equations, etc

# In[1]:


import numpy as np


# ### Numerical analysis

# In[2]:


a = np.array([1, 2, 3], dtype='int8') # Creates 2x3 matrix
print(a)


# In[3]:


print(a.ndim) # dimensions


# In[4]:


print(a.shape) # n x m


# In[5]:


print(a.dtype) # datatype


# In[6]:


print(a.itemsize) # size of each item


# In[7]:


print(a.nbytes) # total size


# In[8]:


c = np.array([[1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50 ,60, 70]], dtype='int8') # you can change dtype to float, double, etc
print(c.shape)


# In[9]:


print(c[0, 1]) # print value at 1st row 2nd column


# In[10]:


print(c[1, :]) # print second row


# In[11]:


print(c[:, 0]) # print valules of all rows 1st column


# In[12]:


print(c[1, 1:6:2]) # print values at 2nd row 1 to 6 step of 2 (i.e. value at 1, 3, 5)


# In[13]:


c[0,5] = 8 # modify particular value
c


# In[14]:


arr = np.zeros((2,3), dtype='int8') # 2x3 matrix with all zeros
arr


# In[15]:


arr = np.ones((2, 2), dtype='float') # 2x2 matrix with all ones
arr


# In[16]:


arr = np.full((2,3), 3) # 2x3 matrix with all 3 # np.full((shape), value)
arr


# In[17]:


arr = np.random.randint(1,100, size=(2,3)) # 2x3 matrix with random values between 1 to 100.
arr


# In[18]:


arr = np.identity(3, dtype='int8') # 3x3 identity matrix
arr


# In[19]:


a = np.repeat(3, 4) # repeat elements of array (3 4 times)
print(a)
arr = (([1,2],[2,3]))
a = np.repeat(arr, 4)
print(a)
a = np.repeat(arr, 3, axis=0) # axis 0 rows axis 1 columns
print(a)
a = np.repeat(arr, 3, axis=1)
a


# In[20]:


b = np.array(((([3,4,5],[1,4,3],[5,6,7],[9,0,8])))) # 4x3 array
b


# ### Arithmetic Operations
# Operarions
# +
# -
# *
# /
# **
# sin
# cos ...
# #### https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html

# In[21]:


a = np.array([1, 2, 3, 4])
np.cos(a)


# In[22]:


np.sin(a)


# In[23]:


b = np.array([5, 6, 7, 8])
a+b


# In[24]:


a-b


# In[25]:


a*b


# In[26]:


a**b


# In[27]:


a/b


# In[28]:


a = np.array([2,3])
b = np.array(([3,5], [2, 4]))
a*b


# In[29]:


a = np.ones((2,3))
b = np.full((3,2), 2)
# a*b Error will occur so we have to use matmul()
np.matmul(a,b)


# In[30]:


a = np.array([2,5,7,9,3,10,45,78,3])
np.max(a)


# In[31]:


np.min(a)


# In[32]:


np.mean(a)


# ### Reorganizing Arrays

# In[33]:


a = np.array([2,5,7,9,3,10,45,78,3])


# In[34]:


np.reshape(a, (3,3)) # change dimensions to 3x3 


# In[35]:


np.arange(10).reshape(2,5) # rearange 0-9 to 2x5 matrix


# In[36]:


b = np.vstack(a) # stacking all elements vertically or in rows
b


# In[37]:


x = np.hstack(b) # stacking all elements horixontally or in columns
x


# In[38]:


np.vstack([b, b]) #a, b are two np arrays


# In[39]:


np.vstack([a, a]) #a, b are two np arrays


# In[40]:


##### Load data from File #######
# You can load file with data as follow
# file = np.getfromtxt("filename", delimiter="del")
# file.astype('int32') #specify any datatype
# file[file > 50] # value greater than 50 you can do all operations which are permitted on numpy


# In[41]:


#get list from array
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a[[1,4,8]])


# In[42]:


print(np.any(a % 2, axis=0)) #axis = dimension returns bool if condition matches


# In[43]:


print(np.all(a % 2, axis=0)) #axis = dimension


# In[44]:


print((a > 3) & (a < 9)) #returns bool


# ### Linear Algebra
# Link - https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

# In[45]:


m = np.array(((([3,4,5],[1,4,3],[5,6,7],[9,0,8]))))
m


# In[46]:


m = np.matrix([[3,4,5],[1,4,3],[5,6,7],[9,0,8]]) # same as np.array see the documentaion for more details
m


# In[47]:


x = m.T # transpose of matrix.. swap rows to column
x


# In[48]:


p = m.I # Inverse the matrix.. reciprocal of a number.. Read Matrix Inverse - Link - https://www.mathsisfun.com/algebra/matrix-inverse.html
p


# In[49]:


s = np.matrix([2,3])
p = s.I
p


# In[50]:


a = np.matrix([5]) # 1 devide by number is reciprocal so 1/5 = 0.2. But please read about matrix inverse 
a.I


# In[51]:


# check if inverse calculates is correct or not by following formula
# original matrix * inverse matrix should produce identity matrix
m = np.matrix([[3,4,5],[1,4,3],[5,6,7]])
print(m.I)
m*m.I


# In[52]:


np.eye(5) # same as np.identity(5)


# In[53]:


a = np.matrix([[2,4], [5,6]])
b = np.matrix([[5,1], [7,8]])
np.dot(a, b) # dot product of matrix

