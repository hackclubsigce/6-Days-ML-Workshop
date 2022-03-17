#!/usr/bin/env python
# coding: utf-8

# # String operations in python

# ## 1.Slicing operation

# In[ ]:


# A = "Hack_Club_SIGCE"


# In[ ]:


print(A[2:9])


# In[ ]:





# ### Slice From the Start

# In[ ]:


print(A[:5])


# In[ ]:





# ### Slice From the Start

# In[ ]:


print(A[5:])


# In[ ]:





# ## 2.Modify Strings

# ### Upper Case

# In[ ]:


print(A.upper())


# In[ ]:





# ### Lower Case

# In[ ]:


print(A.lower())


# In[ ]:





# ### Replace String

# In[ ]:


print(A.replace("_", "-"))


# In[ ]:





# ## 3.Concatinate Strings

# In[ ]:


a = "Krutika"
b = "Vinchu"
c = a + b
print(c)


# In[ ]:





# ## 4.Format - Strings 

# In[ ]:


age = 36
txt = "My name is John, I am " + age
print(txt)


# In[ ]:


age = 20
txt = "My name is Krutika, and I am {}"
print(txt.format(age))


# In[ ]:


no_of_days = 5
current_day = 3

HackClubSIGCE = "It is a {} rd day session of  {} days with python workshop."
print(HackClubSIGCE.format(current_day, no_of_days))


# In[ ]:





# In[ ]:





# ## Methods  

# ### Count Method 

# In[ ]:


txt = "I am Krutika, and I am 20"
count1 = txt.count("am")
print(count1)


# In[ ]:





# ### Capitalize Method 

# In[ ]:


txt = "i am krutika, and i am 20"
count2 = txt.capitalize()

print (count2)


# In[ ]:





# In[ ]:





# # Python Lists

# In[ ]:





# ### Create a List 

# In[ ]:


mylist = ["Vedanti", "Shree", "Krutika"]
print(mylist)


# In[ ]:





# ### List Length

# In[ ]:


print(len(mylist))


# In[ ]:





# ## 1.Access Items 

# In[ ]:


print(mylist[1])


# 

# ### Negative Indexing 

# In[ ]:


print(mylist[-1])


# In[ ]:





# ### Range of Indexes 

# In[24]:


print(mylist[1:2])


# In[ ]:





# ## 2.Change Item Value 

# In[ ]:


mylist = ["Vedanti", "Shree", "Krutika"]
mylist[1] = "Sidhhi"
print(mylist)


# In[ ]:





# ## 3.Add List Items 

# In[ ]:


mylist.append("Shree")
print(mylist)


# In[ ]:





# ## 4.Remove List Items 

# In[ ]:


mylist.remove("Krutika")
print(mylist)


# In[ ]:





# # Python Tuple 

# In[ ]:





# ## Creating tuple

# mytuple1 = ("Hack", "Club", "SIGCE")
# print(mytuple1)

# In[ ]:





# ### Access Tuple Items 

# In[ ]:


print(mytuple1[1])


# In[ ]:





# ### Negative Indexing 

# In[ ]:


print(mytuple1[-1])


# In[ ]:





# ## Update Tuples

# ### Add Items 

# In[ ]:


y = list(mytuple1)
y.append("2021")
mytuple1 = tuple(y)
print(mytuple1)


# In[ ]:





# ## Tuple Methods

# ### count () method in tuple

# In[40]:


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)


# In[ ]:





# ### Tuple index() Method 

# In[ ]:


x = thistuple.index(8)


# In[ ]:





# ## Dictionary

# ### creating a dictionary 

# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[ ]:





# ### Access elements in a dictionary 

# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# In[ ]:





# ### Update Dictionary Items 

# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


# In[ ]:





# ### Add items in a dictionary

# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) 


# In[ ]:





# ### Remove Dictionary Items

# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# In[ ]:





# ## Sets in python 

# ### creating a set 

# In[ ]:


myset = {"apple", "banana", "cherry"}
print(myset)


# In[ ]:





# ### add items in a set 

# In[ ]:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[ ]:





# ###  remove set elements

# In[ ]:


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# In[ ]:





# # Type conversion  

# In[ ]:





# ## Implicitly 

# In[ ]:



x = 10
 
print("x is of type:",type(x))
 
y = 10.6
print("y is of type:",type(y))
 
x = x + y
 
print(x)
print("x is of type:",type(x))


# In[ ]:





# ## Explicitly 

# In[ ]:


s = 'ABCDE'
 
# printing string converting to tuple
c = tuple(s)
print ("After converting string to tuple : ",end="")
print (c)


# In[ ]:





# In[ ]:


# printing string converting to list
c = list(s)
print ("After converting string to list : ",end="")
print (c)


# In[ ]:





# # Array Operations

# In[ ]:





# ## creating array

# In[ ]:


import array as arr
 
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
 
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()


# In[ ]:





# ## inseting into array 

# In[ ]:


# insert() function
a.insert(1, 4)
 
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()
 


# In[ ]:





# ## Accessing element in array 

# In[ ]:


# accessing element of array
print("Access element is: ", a[0])


# In[ ]:





# ## Remove element from array 

# In[ ]:


# using pop() to remove element at 2nd position
print ("The popped element is : ", end ="")
print (arr.pop(2))


# In[ ]:





# In[ ]:


type(a)


# In[ ]:





# In[ ]:





# In[ ]:




