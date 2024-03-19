#!/usr/bin/env python
# coding: utf-8

# ### Numpy

# In[1]:


#  First import the library using the following code:

import numpy as np


# In[3]:


age_list = list(np.random.randint(20,60,10))
print(type(age_list))
print(age_list)


# In[6]:


# 1D Array

age_array = np.array(age_list)
print(type(age_array))

print(age_array)

print(age_array.ndim)  # Provides the dimention of the array
print(age_array.size)  # Provides the number of elements in the array
print(age_array.shape) # Provides the shape of the array


# In[20]:


# 2D Array
two_array = age_array.reshape(2,5)
print(two_array)


# In[ ]:





# In[9]:


books = np.array(['Python for Data Science', 'Intro to machine learning', 'Intro to deep learning'])

print(books)
print(type(books))
print("The shape of the array is:", books.shape)


# ** Random()** is used to create random numbers. It will create the random numbers from [0.0,1.0]

# In[19]:


one_rand_nos = np.random.random(size=20)
print(one_rand_nos)



two_rand_nos = np.random.random(size = (3,4))
print("\n", two_rand_nos)


two_rand = one_rand_nos[:12].reshape(4,3)
print("\n", two_rand)


# In[29]:


# Three Dimentional Array:

three_rand_nos = np.random.random(size=(3,4,4))
print(three_rand_nos)


# In[32]:


print("The size of 3D array:", three_rand_nos.size)
print("\nThe Dimension of 3D array:", three_rand_nos.ndim)
print("\nThe shape of the array is:", three_rand_nos.shape)


# In[106]:


np.random.randint(-20,-10,10)


# In[36]:


np.random.rand(10)


# In[37]:


numpy.arrange()

start = starting number
stop = ending number


# In[41]:


odd_nos = np.arange(1,101,2)
print(odd_nos)

even_nos = np.arange(0,100,2)
print("\n",even_nos)


# In[52]:


# Creating evenly spaced numbers using linspace:
print(np.linspace(0,100,5))
print(np.linspace(0,100,10))


# Creating zero array
print(np.zeros(10))    # It can be only 1-dimension array.
print(np.zeros((10,2)),int)

# Creating one array
print(np.ones(10))     # It can be only 1-dimension array.


# In[53]:


# Creating the 3 x 3 matrix

print(np.full((3,4), fill_value=5))


# In[54]:


# Creating the identity matrix:

print(np.identity(4))


# In[58]:


# np.eye (Rows, columns, Identify index):

np.eye(4,5,0)    # It will also create the identity matrix with identity in the kth index


# In[59]:


another_arr = np.random.randint(10,100,20).reshape(5,4)
print(another_arr)


# In[62]:


# Matrix multiplication Matrix

another_arr.dot(np.eye(4,5,0))


# In[67]:


odd_number = np.array([1,3,5,7]).reshape(2,2)
even_number = np.array([8,6,2,4]).reshape(2,2)

print(odd_number,"\n\n",even_number)


# In[71]:


#  Multiplication of two arrays:
print(odd_number * even_number)


# Scalar Multiplication:
print("\n\n",odd_number * 5)


# In[72]:


# Matrix Multiplication:

print(odd_number.dot(even_number))


# In[91]:


salaries = np.random.randint(10000,1000000,60).reshape(6,10)
print(salaries)


# In[95]:


my_matrix = np.random.randint(10,20,16).reshape(4,4)
my_matrix


# In[96]:


np.flip(my_matrix)


# In[97]:


np.flipud(my_matrix)


# In[102]:


print(np.flip(my_matrix,0))

print("\n",np.flip(my_matrix,1))


# In[ ]:




