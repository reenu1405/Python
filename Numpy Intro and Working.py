#!/usr/bin/env python
# coding: utf-8

# ## Python Numpy(Numerical Python) :

# In[1]:


import numpy as np


# In[6]:


# numpy is fast, looks like list but faster than list
a = [1,2,3]
a_array = np.array(a)
a_array.dtype


# In[7]:


print(a_array)


# In[9]:


a1 = [1,2.1,3]
a1_array = np.array(a1)
a1_array.dtype


# In[8]:


print(a1_array)


# In[ ]:


# numpy can hold only a fixed data type 
# while in list we can have diff elements


# In[10]:


#diff dimensions of an array
a1_array.ndim # ndim tells the dimensions of an array


# In[14]:


a2 = [[1,2,3],[1,2,3]]
a2_array = np.array(a2)
a2_array.dtype


# In[15]:


a2_array.ndim # this is two dimensional array


# In[16]:


a2_array.shape


# In[17]:


a = [[1,2,3],[4,5,6]]
a_array = np.array(a)
a_array.size


# In[18]:


a_array


# In[19]:


# access elements in array= a_array[row,column]
a_array[0,2]


# In[34]:


a = [[[1,2,33],[3,4,11]],[[4,5,55],[6,0,66]],[[7,8,77],[9,10,99]]]
a_array = np.array(a)
a_array.ndim
a_array


# In[35]:


a_array[2,0,1] #access the elements
a_array[2::]
a_array[:,1]


# In[36]:


# assign a value or change a value
a_array[2,1,1]=56
a_array


# In[37]:


a_array.shape


# In[38]:


#initialize arrays
b_aaray = np.zeros(5, dtype = "int32") # by default it will create float type but we can mention the datatype as int or as we want
b_aaray


# In[39]:


# we can create diff dimensions array
b_aaray = np.zeros((3,3), dtype = "int64")
b_aaray


# In[40]:


b_aaray = np.ones((3,3), dtype = "int32")
b_aaray


# In[41]:


b_aaray = np.full((3,3), 99) # if we want any number then use full
b_aaray


# In[42]:


# array of random decimal values
c_array = np.random.rand(2,3)
c_array


# In[45]:


# array of identity matrics : all the diagonal will be one
c_array = np.identity(5, dtype = "int32")
c_array


# In[44]:


type(c_array) # this is the object of ndarray class


# In[47]:


#Mathematics
c_array = np.identity(3, dtype = "int32")
c_array


# In[52]:


c_array+3


# In[59]:


c_array = np.identity(3, dtype = "int32")
c_array


# In[62]:


d_array = c_array.copy()
d_array


# In[64]:


d_array[0,0]=9
d_array


# In[66]:


c_array*2


# In[67]:


a_array1 = np.full((2,3), 9, dtype='int32')
a_array2 = np.full((2,3), 5, dtype='int32')
print(a_array1)
print(a_array2)


# In[68]:


a_array1 + a_array2


# In[69]:


#trignometry
c_array = np.identity(3, dtype = "int32")
np.sin(c_array)


# In[70]:


a = [[1,2,3],[4,5,6]]
a_array = np.array(a)
a_array


# In[73]:


np.min(a_array)
np.max(a_array)
np.mean(a_array)


# In[74]:


np.min(a_array , axis=0) #by passing axis it will give the min for each column
#axis=0 is column , axis=1 is for row


# In[75]:


np.min(a_array , axis=1)


# In[76]:


a_array1 = np.full((2,3), 9, dtype='int32')
a_array2 = np.full((2,3), 5, dtype='int32')
print(a_array1)
print(a_array2)


# In[77]:


# stacking multiple arrays
np.vstack((a_array1,a_array2)) # vertical stacking of two arrays


# In[78]:


np.hstack((a_array1,a_array2)) # horizontal stacking of two arrays


# In[87]:


# create array from a file
f = np.genfromtxt('C:/Users/MY DEVICE/Desktop/nparray.txt', delimiter = ',' ,dtype ='int32')
f


# In[93]:


#advance indexing
f<20
f[f>20]
f[(f>20) | (f<50)] # or : either one
f[(f>20) & (f<50)] # and : both should be apply


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




