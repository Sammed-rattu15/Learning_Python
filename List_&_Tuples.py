#!/usr/bin/env python
# coding: utf-8

# ### List and Tuples

# In[20]:


# Creating a list
mylist = [1, 2, 45, 60, 7, 30, 10, 5, 6, 8]
print(mylist)


# In[21]:


mixed_list = [1, 2, True, 'Mystring']
print(mixed_list)


# In[2]:


# Importing numbers from numpy and generating random numbers:
import numpy as np
my_numbers = np.random.randint(10,100,100)
print(my_numbers)


# In[3]:


my_num_list = type(my_numbers)
print(my_num_list)


# In[4]:


#  Converting numpy.ndarray into a list:
my_num_list = list(my_numbers)
print(type(my_num_list))


# In[5]:


print(my_num_list)


# In[6]:


index = 4
my_num_list[index]


# In[7]:


# Get the length of numbers using len():

len(my_num_list)
print(list(range(len(my_num_list))))


# In[8]:


# Print the odd numbers from the number list using a loop:
for i in range(len(my_num_list)):
    if my_num_list[i] % 2 > 0:
        print(my_num_list[i],end=" ")


# In[9]:


# Print the odd & even numbers from the number list using a loop:

my_odd_list = []
for i in range(len(my_num_list)):
    if my_num_list[i] % 2 > 0:
        my_odd_list.append(my_num_list[i])
print(my_odd_list)

my_even_list = []
for j in range(len(my_num_list)):
    if my_num_list[j] % 2 == 0:
        my_even_list.append(my_num_list[j])
print(my_even_list)


# In[10]:


print("My odd number list is:\n", my_odd_list)
print("\n","Number of odd numbers in the list is: ", len(my_odd_list))

print("\n""My even number list is: \n", my_even_list)
print("\n","Number of even numbers in the list is: ", len(my_even_list))


# In[11]:


my_odd_list = []
my_even_list = []
for i in range(len(my_num_list)):
    if my_num_list[i] % 2 > 0:
        my_odd_list.append(my_num_list[i])
    else:
        my_even_list.append(my_num_list[i])
print("My odd number list is:\n", my_odd_list)
print("\n","Number of odd numbers in the list is: ", len(my_odd_list))

print("\n""My even number list is: \n", my_even_list)
print("\n","Number of even numbers in the list is: ", len(my_even_list))


# In[12]:


#  Creating a Tuple

my_tuple = (1, 2, 5, 10, 20)
print(my_tuple)
print(type(my_tuple))


# In[13]:


my_tuple[0]


# In[14]:


my_new_list = []
print("Length of my new list is: ",len(my_new_list))


# In[15]:


# Combination of 2 lists in 1 using Extend function:

list1 = list(np.random.randint(10, 100, 50))
list2 = list(np.random.randint(100, 1000, 50))
print(list1)
print(list2)


# In[16]:


list1.extend(list2)


# In[17]:


print(len(list1))


# In[22]:


mylist = [1, 2, 45, 60, 7, 30, 10, 5, 6, 8]
print(mylist)


# In[23]:


mylist.insert(9, 5)


# In[24]:


print(mylist)


# In[25]:


# removal of elements:



# In[29]:


#  Commen list Operations

# Checking the existanceof an element in a list 

print("Length of List 1: ", len(list1))

check_element  = int(input())

print("The existance of {} in list 1: The result is = {}".\
      format(check_element, (check_element in list1)))


# In[30]:


# List manipulation:
my_subset = list1[0:10]
print(my_subset)
# Reversing element in my subset
print("Before reversing the element: ", my_subset)

my_subset.reverse()
print("After reversing the element: ", my_subset)


# In[31]:


# Sorting the elements

print("Before sorting the elements: ", my_subset)

my_subset.sort()
print("\nAfter sorting the element in Ascending order: ", my_subset)

my_subset.sort(reverse= True)
print("\nAfter sorting the element in Decending order: ", my_subset)


# In[32]:


#### Slicing and Indexing

name = "Python"

print("Printing the last element using negative indexing: ", name[-1])

print("list with skipped elements: ", name[::2])


# In[33]:


matrix = [[1,2,3], [4,5,6], [7,8,9]]

# Accesing the first element:
matrix[0]

# Accesing the inner elements of an list:
matrix[0][1]


# In[34]:


# Using list Comprehension:

my_odd_list = [num for num in my_num_list if num % 2 >0]
print("Number of odd numbers in the list is: ",my_odd_list)

my_even_list = [num for num in my_num_list if num % 2 == 0]
print("\n""Number of even numbers in the list is: ",my_even_list)


# In[35]:


### Sum of matrix elements:

matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix_sum = [sum(lst) for lst in matrix]
print(matrix_sum)


# In[36]:


tup1 = (1, 2, 3)
tup2 = ('a', 'b')
tup3 = True, False

print(type(tup3))


# In[37]:


## Concatenation of Tuples:

com_tuple = tup1 + tup2 + tup3

print(com_tuple)


# In[38]:


## Repetation Operation:

print("Repetation operation: ", tup1 * 3)


# In[39]:


## 

my_tuple = [num * 2 for num in tup1]
print(my_tuple)

for ele in my_tuple:
    print(ele)


# In[ ]:





# # HANDS ON PRACTICE: LISTS

# In[40]:


# You are provided with a list of student scores in a class. Perform the following operations:

student_names = ["John", "Mary", "Messi", "Zaltan"]
scores = [75, 86, 80, 92, 90]

# Find and display the highest score in the class.
highest_scores = max(scores)
print("The highest score in the class is: ", highest_scores)

# Calculate and print the average score of the class.
average_score = sum(scores)/len(scores)
print("The average score in the class is: ", average_score)

# Identify and display the names of students who scored above a certain threshold (e.g., 80).
threshold = 80
above_threshold = [name for name, score in zip(student_names, scores) if score > threshold]
print(f"Students scoring above {threshold}: {above_threshold}")

# Sort and display the student names in alphabetical order.
display_name = sorted(student_names)
print(f"The sorted names are:", display_name)


# In[41]:


# Generate Squares and Cubes

# Write a program to generate two lists using list comprehension. The first list should contain the squares of numbers from 1 to 10, and the second list should contain the cubes of the same numbers.

# List to generate square & cubes:

squares = [x**2 for x in range(1,11)]
cubes = [x**3 for x in range(1,11)]

# Execute the block of code:

print(f"The squares are: ", squares)
print(f"The cubes are: ", cubes)


# In[42]:


# Filtering Positive Numbers

# Given a list of numbers, create a new list that contains only the positive numbers from the original list. Implement this using list comprehension.

# Sample list of numbers:
numbers = [-1, 3, -9, -4, -6, -7, 6, 8, 10]

# List Comprehension method:
positive_numbers = [num for num in numbers if num > 0]

# Execute the block of code:

print("Original numbers: ", numbers)
print("Positive numbers: ", positive_numbers)


# In[43]:


# Sorting Student Names

# You have a list of student names. Implement a program to sort the names alphabetically and display the sorted list.

student_names = ["Alice", "Bob", "Messi", "Zaltan", "Ronaldo", "Neymar"]

# Sorting List Method:

sorted_names = sorted(student_names)

# Execution of code:

print("Original list: ", student_names)
print("Sorted list: ", sorted_names)


# In[ ]:





# # HANDS ON PRACTICE: TUPLES

# In[44]:


# You are managing student course enrollments, and each course has a unique identifier, a list of enrolled students, and their corresponding grades. Implement a program using advanced tuple operations to perform the following:


# Create a tuple for a course containing its identifier, a list of enrolled students, and their grades.
course_info = ("CS101", ["Alice", "Bob", "Charlie"], [90, 85, 92])

# Display the course information, including the average grade.
course_id, students, grades = course_info
average = sum(grades)/len(grades)
print(f"Course information for {course_id}:\nName: {students}:\nGrades: {grades}:\nAverage grade is: {average}")

# Identify and display the student with the highest grade in the course.
highest_score = students[grades.index(max(grades))]
print(f"\nThe student with highest score is: {highest_score}")

# Update the grade of a specific student.
upgrade_list = list(grades)
upgrade_list[1] = 89
course_id, students, grades = course_info
print(f"\nUpdated Course information for {course_id}:\nName: {students}:\nGrades: {upgrade_list}:\nAverage grade is: {average}")


# In[58]:


# Filtered Student Information 

# You have a list of student names, their ages, and their grades. Implement a program using tuple comprehension and filtering to perform the following:
student_names = ["Alice", "Bob", "Charlie", "Delta"]
ages = [20, 23, 16, 25]
grades = [85, 90, 78, 92]

# Create a list of tuples where each tuple contains a student’s name, age, and grade.
new_student_list = [(names, age, grade) for names, age, grade  in zip(student_names, ages, grades)]
print(new_student_list)

# Display the list of student tuples.
print("\nList of student tuples:", new_student_list)

# Filter and display only the information of students who are above a certain age.
filtered_student_list = [(names, age, grade) for names, age, grade in new_student_list if age > 20]
print("\nNew filtered student list:", filtered_student_list)


# In[1]:


#Employee Salary Calculation

# You have a list of employees, and each employee is represented as a tuple containing their name, hourly rate, and hours worked./
# Implement a program using tuple unpacking and functions to perform the following:
employees = [("Charlie", 90, 40), ("Bob", 58, 35), ("Alice", 75, 38)]

# Calculate and display the total salary for each employee.
def emp_total_salary(rate, hours):
    return rate * hours

total_emp_salary = [emp_total_salary(rate, hours) for _, rate, hours in employees]
print("Total Salary is: ",total_emp_salary)


# Identify and display the employee with the highest total salary.
highest_salary = employees[total_emp_salary.index(max(total_emp_salary))]
print("Highest Salary: ", highest_salary)

# Display the average total salary of all employees.
average_salary = sum(total_emp_salary)/ len(employees)
print("Average Salary: ", average_salary)


# In[30]:


# STUDENT GRADE BOOK:
grade_book = {"Alice": (85, 90, 92), "Bob": (78, 85, 88), "Charlie": (90, 92, 95)}

# Display the student names and their average scores.
average_score = {name: sum(scores)/ len(scores) for name, scores in grade_book.items()}
print("Average Score is:", average_score)

# Identify and display the student with the highest average score. 
highest_score = max(average_score, key= average_score.get)
print(highest_score)

# Display the average scores for each subject.
subject_names = ["Subject1", "Subject2", "Subject3"]
subject_averages = {subject: sum(grade_book[name][i] for name in grade_book) / len(grade_book) for i, subject in enumerate(subject_names)}
print("Subject Average Scores:", subject_averages)


# In[10]:


num = 0
while num <= 100: 
    print(num, end=" ")  # (n =0 , n-1)
    num+=1


# In[19]:


fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(fruit)

