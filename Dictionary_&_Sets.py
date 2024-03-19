#!/usr/bin/env python
# coding: utf-8

# # DICTIONARIES

# In[21]:


# Creating a Dictionary:

mydict = {'name':'Shaw', 'age':58, 'gender':'male'}

print(type(mydict))


# In[22]:


# Accesing the Keys and values from the dictionay:

mydict_keys = mydict.keys()  ## Extracting the keys fromt the dict.
mydict_values = mydict.values()  ## Extracting the Values fromt the dict.
mydict_items = mydict.items()   ## Extracting the Items fromt the dict.

print("Keys: ", mydict_keys, "\nValues: ", mydict_values)


# In[23]:


# Accesing the items from the dictionary:

for key, value in mydict.items():
    print("Keys: ", key)
    print("Values: ", value)


# In[24]:


# Accesing the items from the dictionary:
for item in mydict.items():
    print("Items: ", item)


# In[25]:


# Reversing the items in the dictionary:

swapped_dict = {(value, key) for key, value in mydict.items()}
swapped_dict


# In[26]:


# Adding the element in the dictionary:

mydict['location'] = 'Bangalore'
print(mydict)


# In[27]:


# Creating the empty dictionary:

new_dict1 = {}
new_dict2 = {}

new_dict1['first'] = 1
new_dict2['second'] = 2
print(new_dict1, new_dict2)


# In[28]:


# Updating a dictionary with another dictionary:

student_info = {'name': 'Alice', 'age': 22, 'grade': 'A'}
student_info['city'] = 'New York'  ## Add a new key-value pair:

student_info


# In[29]:


additional_info = {'city': 'Boston', 'marks': 95}
student_info.update(additional_info)

student_info


# In[30]:


## Dictionary with multiple values for a key:

student = {'name': ['Shan', 'Sam', 'Ajith'], 'gender':['male', 'male', 'male']}
student


# In[31]:


student['name'][2] = 'Lucy'
student['gender'][2] = 'female'

student


# In[32]:


## Removal of a particular key 
student_info


# In[33]:


student_info.pop('age')
student_info


# In[34]:


# Using "popitem" to remove a key, value pair from a dict:

popped_items = student_info.popitem()
popped_items


# In[35]:


# Using "del" to remove a key, value pair from a dict:
print(student_info)
del student_info['grade']
print(student_info)


# In[36]:


## Checking the "Keys", "Values" & "items" present in dict

student_info = {'Name': 'Alice', 'Age': 22, 'Grade': 'A'}
student_info['City'] = 'New York'  ## Add a new key-value pair:

student_info


# In[37]:


# Checking age present in keys
print('age' in student_info)


# In[38]:


additional_info1 = {'Last Name': 'Morgan'}
student_info.update(additional_info1)

print(student_info)


# In[39]:


# Sorting of dict using the "sorted" method:

sorted_student_info = dict(sorted(student_info.items()))

print(sorted_student_info)


# In[40]:


square_dict = {x:x**2 for x in range(1,6)}

print(square_dict)


# In[ ]:


Keys = ['name', 'age', 'city']
values = ['John', 28, 'Chelsea']


# In[60]:


emp = {"John": 4000, "Sam": 9000, "Max": 6800, "Paul": 8800, "Jack": 2800}

emp_key = emp.keys()
emp_values = emp.values()
emp_items = emp.items()

# Find the highest salary from the above dict:
highest_salary = max(emp_items)
print("The employee with highest salary is: ", highest_salary)

# Find the average of salary in the above dict:
average = sum(emp_values)/len(emp_values)
print(f"the average salary is: ", average)

# Identify and display the names of students who's salary is above a certain threshold:
threshold = 4000
above_threshold = [key for key, value in emp_items if value > 4000]
print("Employees who can earn more salary: ", above_threshold)


# # SETS

# In[73]:


#  Creating the sets:

num =np.random.randint(10, 100, 25)
num


# In[74]:


print(len(num))


# In[75]:


#  Creating the set using set()

num_set = set(num)
print(type(num_set))
print(num_set)


# In[76]:


num_set1 = {18, 23, 10, 18, 28, 28, 15, 18, 21}
print(num_set1)


# In[78]:


# Addition of another set in exisiting set using update method:

num_set.update(num_set1)
print("Length of combined set: {} and \nThe combined set is {}". format(len(num_set), num_set))


# In[97]:


## SET OPERATIONS:

# Creating two new sets:

num_set2 = set(np.random.randint(10, 100, 25))
num_set3 = set(np.random.randint(10, 50, 25))

print("Set 1: ", num_set2)
print("Set 2: ", num_set3, f"\n")

print("Length of Set 1: ", len(num_set2))
print("Length of Set 2: ", len(num_set3))


# In[98]:


combined_set = num_set1 | num_set2
print("Number of elements in combined set: ", len(combined_set))


# In[100]:


print(num_set1.union(num_set2))


# In[99]:


# Intersection Operation:

common_elements = num_set1 & num_set2
common_elements


# In[104]:


# Difference Operation:

difference_elements = num_set1 - num_set2
print(difference_elements)

print(num_set1.difference(num_set2))


# Extra Exercise of Strings:

# In[142]:


date = '21', 'Jan', '2023'
# Join method will help to join the elements:
'-'.join(date)


# In[147]:


str1 = "Indranil-Bokachoda"
firstname, lastname = str1.split('-')
print(str1)

print("\nFirst Name: {}, Last Name: {}".format(firstname,lastname))


# In[159]:


sen = "I love using cars for long drive# ! ~ ) &"
import string
print(string.punctuation)

len([ltr for ltr in sen if ltr not in string.punctuation + ' '])


# In[160]:


len([ltr for ltr in sen if ltr.isalpha()])


# In[ ]:





# In[ ]:





# # HANDS ON EXERCISE:

# In[30]:


# You are provided with a dictionary containing employee names and their corresponding monthly salaries. 
employees = {
    "Bob": 4500, 
    "Max": 8500, 
    "Charlie": 6500, 
    "Alice": 9000
}

# Find and display the highest salary in the company. 
highest_salary = max(employees.values())
print("Highest Salary of an employee is:", highest_salary)

# Calculate and print the average salary of all employees. 
average_salary = sum(employees.values()) / len(employees.values())
print("The average salary of an employee is:", average_salary)

# Identify and display the names of employees who earn above a certain threshold (e.g., $5000). 
threshold = 5000
above_threshold = [name for name, salary in employees.items() if salary > threshold]
print("The employees above threshold amount is:", above_threshold)

# Sort and display the employee names in alphabetical order.
sorted_employees = sorted(employees.items())
print("The sorted-list is:", sorted_employees)


# In[60]:


# Extend the dictionary to include the age of each employee. 

# Find and display the oldest employee in the company. 


# Calculate and print the average age of all employees. 


# Identify and display the names of employees who are younger than a certain age (e.g., 30). 


# Sort and display the employee names based on age in ascending order.


# In[ ]:





# In[144]:


# You have a set representing students enrolled in a Computer Science course. 

cs_students = set(['CS_'+str(num) for num in np.random.randint(1000, 2000, 10)])
maths_student = set(['M_'+str(num) for num in np.random.randint(1000, 2000, 10)])
print("\nCS Students List:", cs_students)
print("\nMaths Students List:", maths_student)

# Update the set with students from the Mathematics course.
cs_students.update(maths_student)
print("\nNew Student List:", cs_students)

# Create a copy of the set. 
combined_students = cs_students.copy()
print("\nCombined Students List:", combined_students)

# Add a new student who just joined the course. 
cs_students.add('N-1249')
print("\nCS Student list after adding N_1249:", cs_students)

# Remove a student who dropped the course (handle the case where the student is not in the set). 
cs_students.discard('CS_1483')
print("\nCS Students List after removing CS_1483:", cs_students)

# Discard a student who is not actively participating (no error if the student is not present). 
cs_students.discard('M_1896')
print("\nCS Students List after Discarding M_1896:", cs_students)

# Clear all students from the set.
cs_students.clear()
print("\nCS Students List after Clearing:", cs_students)


# In[ ]:




