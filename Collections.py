
# coding: utf-8

# # List

# **List** holds collections of objects. The *objects* can be integers, floats, strings, characters, boolean values or another list.

# In[30]:


L0 = [] #An empty list
L1 = [2, 3, 9, 6, 1] #A list of integers
L1 #or we can type print(L1)


# Lists can have elements of different types as well dupliacated elements. 

# In[29]:


L2 = [11.92, 25, "Python", 'e', "Python", False, [1,3,9]] #A list containing varius data types
print(L2)


# ## Indexing in Python
# An index corresponds to the position of an item in the list. Python is a zero based indexing language. 

# In[18]:


L3 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
L3[0] #prints index four from the list


# In[19]:


L3[2]


# ## Negative Indexing 
# Negative indexing can be helpful when enumerating elements from the end of a list, such as the last or penultimate element. 

# In[16]:


L3[-1]


# In[17]:


L3[-2], L3[-3]


# ## Deleting 
# Python has a number of ways for deleting an element from a list.

# In[25]:


L4 = [1, 2, 3, 4, 5]
L4.pop() #deletes the last element from the list


# In[26]:


L4


# In[27]:


L4.pop(2) #delets the second index from the modified list
L4


# Another way to delete elements of a list is to use the *del* keyword.

# In[39]:


L5 = ["Project Management", "Cybersecurity", "Data Science", "Internet of Everything", "Dissertation"]
L5


# In[40]:


del L5[4]
L5


# The list.remove(name) method removes the first matching entry from the list.

# In[41]:


L6 = [10, 20, 30, 40, 50 ,60, 70]
L6.remove(20)
L6


# ## List Constructor
# Using the *list* method on a string generates a list for the letters of that string.

# In[46]:


list("DataScience")


# In[45]:


list("TrueFalse")


# ## Slicing a list in Python
# While indexing allows accessing or deleting a single element from a list, slicing enables doing the same thing to a range of elements. 

# In[47]:


L7 = ["Hello", 12, 3.14, 'j', True, [30, 20, 10]]
L7


# Storing the first three elelments of the above list into a variable called *var1*.

# In[49]:


var1 = L7[0:3] #Slices up to the third index, excluding the third index itself. 
var1


# A handy shortcut for the above slice would be *L7[ : 3]*

# In[50]:


var2 = L7[ : 3]
var2


# We can slices the last few elements of a list using negative indices with a range.

# In[53]:


L7[-2 : ]


# ## Concatenating lists
# Lists can be concatenated in Pyhton using the **+** sign.
# 

# In[42]:


myList1 = [1, 2, 3, 4, 5]
myList2 = [6, 7, 8, 9, 10]
myList1 + myList2


# ## Checking methods available
# We can check the available methods for our list.

# In[61]:


L8 = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds"]
dir(L8) #checks the available methods.


# One of the above methods is called *append* which we can use to add new elements to our list.

# In[62]:


L8.append("Sheffield")
L8


# Another method is called *sort* which we can use to sort our numbers.

# In[64]:


L9 = [3, 7, 1, 20, 9, 12, 15, 2]
L9.sort()
L9


# # Tuples
# A tuple is similar to a list as they both store one ore more objects. However, while lists are mutable  tuples are immutable. 
# 
# We define a tuple using parentheses.   

# In[66]:


T1 = (1, 2, 3, 4, 5) #The syntax of a tuple is different than that of a list. 
T1


# Just like a list, a tuple can hold different types of objects including repeated ones. 

# In[86]:


T2 = (25.3, "Collection", 90, 'T', False, [10,30,90], (1,2,3), 25.3)
T2


# A tuple can be indexed just like a list.

# In[72]:


T2[5], T2[6]


# The *type()* method can be used to check whether a collection is a list of a tuple.

# In[74]:


type(L1)


# In[75]:


type(T1)


# The *len()* method can be used to determine the length of a list or a tuple. 

# In[85]:


len(L1), len(T2)


# Lists are mutable which means they can be changed or modified after creation.

# In[80]:


L10 = [100, 200, 300, 350, 500, 600, 700]
L10[3] = 400 #Sets the 3rd index (fourth element) to 400.
L10


# Tuples are immutable and therefore they cannot be changed after creation.

# In[79]:


T3 = ("January", "Feb", "March", "April", "May", "June")
T3[1] = "February" #Outputs an error


# The *dir* command can be used to check the available methods for a tuple. 

# In[81]:


dir(T3)


# # Sets
# Sets also hold collection of objects, however, set object are unique.

# In[93]:


S1 = {9, 1, 2, 3, 4, 5, 4, 1} #Only unique elements are outputed and in order. 
S1


# Sets in Python hold different data types, excluding lists and other sets.

# In[98]:


S2 = {"Hello", False, 12, 45.6, ("Green", "Red", "Blue")}
S2


# # Dictionaries
# Dictionary elements consist of pair of objects called keys and values. 

# In[111]:


D1 = {"First Name" : "John", "Surname" : "Smith", "Email" : "John.Smith@example.co.uk", "Age": 25}
D1


# Dictionaries hold unique keys which cannot be changed, however, its values can be updated. 

# In[118]:


D1["Surname"] = D1["Last Name"]


# In[112]:


D1["Age"] = 26
D1


# New key-value pairs can be added to an already defined dictionary.

# In[113]:


D1["Occupation"] = "a student"
D1


# Outputting all the keys.

# In[114]:


D1.keys()


# Outputting all the values.

# In[115]:


D1.values()

