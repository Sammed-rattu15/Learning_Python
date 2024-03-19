#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import all the required libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[110]:


pip install xlrd


# In[5]:


import warnings
warnings.filterwarnings('ignore')


# ### DATAFRAME MANUPULATION

# In[154]:


# Reading the files from CSV files

df = pd.read_csv("C:/Users/abhay11/Desktop/Python/Data Visualization with Pandas & Numpy\\ny_weather.csv")
df


# In[111]:


# Reading the files from XLSX files

df_excel = pd.read_excel("C:/Users/abhay11/Desktop/Python/Data Visualization with Pandas & Numpy\Sample_Superstore.xls")
df_excel


# df_returns = pd.read_excel('C:/Users/abhay11/Desktop/Python/Data Visualization with Pandas & Numpy\sample_sales.xlsx',\
#                           sheet_name ='Returns')
# df_reeturns

# In[36]:


df.tail(7)


# In[37]:


df.columns


# In[39]:


df.shape


# In[42]:


# Finding the information from the datasheet

df.info()


# ### Accesing the elements
# 
# There are two ways to access elements from the dataframe. They are **loc** & **iloc**
# - Loc uses row names and coloumns names to access the data.
# - iloc uses row index and column index to access the data

# In[47]:


df.head()


# In[51]:


# Using loc to access the temprature, duepoint and humidity coloumns

df_subset = df[['Temperature', 'DewPoint', 'Humidity']]
df_subset.head()


# In[114]:


df.loc["Temperature", "Humidity", "Event"].head


# In[65]:


# Adding a new column

df["Visibility Kms"] = df['VisibilityMiles']*1.6


# In[66]:


df.head()


# In[71]:


df["Wind Speed Kms"] = df['WindSpeedMPH'] * 1.6


# In[72]:


df.head()


# In[77]:


# To drop the column 

df.drop("Visibility Kms", axis=1, inplace=True)


# In[78]:


df.head()


# In[ ]:





# In[79]:


df


# In[82]:


df.index


# In[ ]:





# ## Checking Missing values

# In[87]:


# Missing Values Coloumns

mv = df.isna().sum()
mv[mv > 0]


# In[89]:


# Total number of missing columns

print("The total number of missing values are:", mv.sum())


# In[90]:


# Fill na with mean values of each column

np.round(df.mean(numeric_only=True),2)


# In[94]:


df['Temperature'].fillna(df.Temperature.mean(), inplace=True)


# In[95]:


df.Temperature


# In[99]:


df.fillna({"DewPoint":19.82, "Humidity":49.64, "Sea Level PressureIn":29.99, "VisibilityMiles":9.25, "WindSpeedMPH":6.30},inplace=True)


# In[100]:


df


# In[102]:


mv = df.isna().sum()
mv


# ### Agregating the data

# # WRITING FILES

# In[117]:


students = pd.read_csv("C:/Users/abhay11/Desktop/Python/Data Visualization with Pandas & Numpy\students.csv")


# In[118]:


professors = pd.read_csv("C:/Users/abhay11/Desktop/Python/Data Visualization with Pandas & Numpy\professors.csv")


# In[124]:


# Writing to a file
students.to_csv("students_new.csv", index=False, header=True)


# In[125]:


students


# In[127]:


professors


# ### Merging two data files

# In[136]:


pd.concat([students, professors])


# In[138]:


# Finding common id between two datas
set(students.id_number).intersection(professors.id_number)


# In[139]:


std_prof = pd.merge(students, professors)
std_prof


# In[141]:


pd.merge(students, professors, how= 'left')


# In[142]:


pd.merge(students, professors, how= 'right')


# In[140]:


pd.merge(students, professors, how= 'outer')


# In[143]:


professors.rename(columns={'id_number':'idnumber'}, inplace=True)


# In[146]:


stdprof = pd.merde(student,professors, left_on='id_number', right_on='idnumber')
stdprof


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Resnaping Data Frame

# In[151]:


df_sales = pd.read_excel("C:/Users/abhay11/Desktop/Python/Data Visualization with Pandas & Numpy\sample_sales.xlsx")
df_sales


# In[202]:


df_sales.sum()


# In[ ]:





# In[195]:


df_sales


# In[208]:


df_sales.sum()


# In[ ]:





# In[ ]:




