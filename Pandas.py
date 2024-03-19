#!/usr/bin/env python
# coding: utf-8

# ### Pandas

# In[1]:


# Pandas designed for data visualization and analysis:

# Offers powerful Data-Frame and series of data structure:

# Panda series:
# One dimention array-like data structure 


# In[37]:


# Creating a Pandas Series:

import pandas as pd
import numpy as np


# In[38]:


l1 = np.random.randint(10,90,10)
print(type(l1))
print(l1)


# In[39]:


# Creating a panda series
s1 = pd.Series(l1)
print("Pandas Series from an array:\n",s1)
print("pandas Series Index: ", s1.index)


# In[40]:


s1[5]


# In[41]:


s1[[0,3,5]]


# In[42]:


print(s1[:5],"\n")    # Using range operation
print(s1[2:8])


# In[43]:


print(len(s1))


# In[44]:


s1[s1>50]    # Subsetting elements using conditions


# In[45]:


s1[(s1<20) | (s1>50)]


# In[46]:


s1.min()   # Finding the minimum value


# In[47]:


s1.mean()    # Finding the average value


# In[48]:


print("Min: {}, Max: {}, Average: {}, STD: {}".format(s1.min(), s1.max(), s1.mean(), np.round(s1.std(), 2)))


# In[52]:


# Finding the missing value count
s1.isna(), s1.isnull().sum()


# In[51]:


s1.mean()


# In[119]:


# Replacing all the missing values with the average of the series:

my_idx = s1[s1.isna()].index 
s1[my_idx] = s1.median()
s1[my_idx]


# In[ ]:





# In[ ]:





# In[120]:


s2 = pd.Series([10,15,12,16,21])
print(s2)

s3 = pd.Series([range(10,100,10)]) 
print(s3)


# In[121]:


# Creating a series

salary = pd.Series(np.array([15000,25000,45000,24000,34000]), index = np.arange(0,10,2))
print(salary)


# ### Custom indexing:

# In[133]:


# Custom indexing:

sal_ind = pd.Series(np.random.randint(10000,100000, 10), index = ['N'+ str(i) for i in np.arange(10)])
sal_ind


# In[134]:


sal = sal_ind.sort_values()
sal


# In[135]:


sal_bonus = np.round(sal * .10)
sal_bonus


# In[136]:


# Salary after incerment(Bonus of 10%)
incl_sal = sal + sal_bonus

incl_sal.sort_values()


# In[137]:


salaries = sal_ind.copy(deep = True)


# In[138]:


salaries.sort_values()


# In[139]:


np.round(salaries[salaries>=50000]*1.05, -2)


# In[140]:


np.round(salaries[salaries<50000]*1.1, -2)


# In[141]:


new_inc = pd.concat([np.round(salaries[salaries>50000]*1.05,-2), np.round(salaries[salaries<50000]*1.1, -2)])
new_inc


# In[ ]:





# In[ ]:





# In[131]:


# Creating student marks-list:

std_marks = pd.Series([450,292,435,298,478],
                     index = ['Anand','Akshay','Chetan','Vikram','Vivek'])
print(std_marks)


# In[132]:


std_marks.sort_values()


# In[ ]:




