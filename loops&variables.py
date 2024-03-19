#!/usr/bin/env python
# coding: utf-8

# ### Loops and Variables

# In[1]:


a = 4
if a>0:
    print("The above statement is true")


# In[16]:


# Finding the eligibility to vote
age = int(input())
if age >= 18:
    print("They are eligible to vote")
else:
    print("They are not eligible to vote")


# In[15]:


# Student grades: 
a = int(input())
if (a>=80):
    print("He got an A")
elif (a>=65):
    print("He got an B+")
elif (a>=50):
    print("He got an C")
else:
    print("He failed in exam")


# In[7]:


age_str = input("Please enter your age:")
age = int(age_str)
print("You will be" + " " + str(age+1) + " " + "years old next year")


# In[12]:


user_colour = input("what is your favourate colour?")
print(f"Your Favourate colour is {user_colour}.")


# In[13]:


# For loop statement
fruits = ["apple", "bannana", "cherry"]
for fruit in fruits:
    print(fruit)


# In[14]:


# Loop statement

# Break statement
for i in range(5):
    if i == 3:
        break
    else:
        print(i)


# In[15]:


# Continue Statement
for i in range(5):
    if i == 2:
        continue
    else:
        print(i)


# In[16]:


# Pass Statement 
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)


# In[18]:


input_str = "Python"
reversed_str = ""
for chr in input_str:
    reversed_str = chr + reversed_str
print("reversed_string", reversed_str)


# In[19]:


input_str = "Python"
reversed_str = ""
for chr in input_str:
    reversed_str = chr + reversed_str
print("reversed_string", reversed_str)


# In[ ]:


#File handling


# In[ ]:


help(bool)


# In[20]:


# User defined Function

def square(x):
    """this function calculates the square of the number.""" #Docstring
    result = x**2
    return result
# Callingthe function
result = square(3)
print(result)


# In[21]:


def greet(name):
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")


# In[22]:


# Variable-length arguments(*args & **kwargs) **kwargs is like a dictionary function

def add(*args):
    result = 0
    for num in args:


# In[23]:


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)


# In[24]:


# Lambda Functions

add = lambda x,y: x+y
print(add(5,3))


# In[25]:


square = lambda x: x**2
print(square(4))


# In[26]:


#map() functions

numbers =[1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#filter() function
numbers =[1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

#sorted() function


# In[27]:


try:
    result = 10/0
except ZeroDivisionError:
    print("Error: Division by zero.")
finally:
    print("this will always execute.")


# In[28]:


def get_user_input():
    try:
        user_input = int(input("Enter an integer:"))
        print(f"User entered:{user_input}")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
    finally:
        print("Execution Completed.")
#Test function
get_user_input()


# In[3]:


# You are developing a web application and want to implement user authentication. How can you use functions to handle user login and validation?

def login(user, password):
        if user == "Sammed" and password == "12345678":
            return True
        else:
            return False

# Example
user_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if login(user_input, password_input):
    print("Login Succesful")
else:
    print("Login Failed.")


# In[ ]:




