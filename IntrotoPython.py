#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("Hello, World!")


# In[2]:


import keyword
print(keyword.kwlist)


# In[3]:


#this is a comment


# In[5]:


'''this is 
 a comment'''


# In[9]:


name = "Jhon"
age = 30

print(name)


# In[7]:


a = 10
print(type(a))
print(id(a))


# In[8]:


a = 42
b = 42
print(a is b) #gives true
print(id(a), id(b)) #id of both a & b are same


# In[15]:


x = 257
y = 257
print(x is y)
print(id(x), id(y))


# In[10]:


a = 1.5
print(type(a))
print(id(a))


# In[13]:


z = 3 +4j
print(type(z))
print(id(z))


# In[14]:


first_name = "John"
last_name = "Doe"
full_name = first_name + "\n" + last_name
print(full_name)


# In[23]:


text = "Python"
print(len(text))


# In[19]:


# Understanding the count of words, it starts from ,-1,0,1
text = "Indranil is a bad boy and always drinks."
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(text[6])
print(text[7])
print(len(text))


# In[53]:


print(text[3:6])
print(text[-4:-2])


# In[6]:


number = "42"
print(type(number))
print(str(number))


# In[7]:


str_number = "42"
integer = str_number
print(int(integer))


# In[22]:


# Converting Cases of a single text.
text = "Python is fun"
upper_text=text.upper()
lower_text=text.lower()
print(upper_text)
print(lower_text)
print(text.capitalize())
print(text.title())


# In[20]:


my_string = "Python is Fun!"
stripped_string = my_string.strip()
print(stripped_string)


# In[51]:


# Finding and replacing any word or number
sentence = "Python is fun and Python is fun"
index = sentence.find("Python")
replace = sentence.replace("Python", "JavaScript")
print(index)
print(replace)


# In[36]:


find = sentence.index("fun")
print(find)


# In[53]:


# Counting the number of words present
sentence = "Python is easy and Python is fun"
count_is = sentence.count("is")
print(count_is)


# In[54]:


text = "Hello World"
starts_with = text.startswith("World")
print(starts_with)


# In[23]:


# Spliting and Joining the sentences
sentence = "Python is easy and Python is fun"

split_sentence = sentence.split()
print(split_sentence)

join_sentence = " ".join(sentence)
print(join_sentence)


# In[24]:


# Use format method to add something to a sentence,For example
name = "John"
age = 25
formatted_string = "My name is {}, and I am {} years old.".format(name, age)
print(formatted_string)


# In[25]:


# Casting and Conversion
value = 0
bool_value = bool(value)
print(bool_value)


# In[26]:


my_list = [('a', 1), ('b', 2)]
print(dict(my_list))


# In[27]:


a = 10
b = 4
print(a&b)
print(a|b)
print(a^b)
print(a)


# In[28]:


x = 10
print(x)


# In[ ]:




