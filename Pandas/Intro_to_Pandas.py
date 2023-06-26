#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dictionary
emp = {'name' : 'Ankit','gender':'Male','email':'ankit@gmail.com'}
emp = {'name' : ['Ankit','Rahul','Priya'],'gender':['Male','Male','Female'],'email':['ankit@gmail.com','rahul@gmail.com','priya@gmail.com']}
emp


# In[2]:


import pandas as pd


# In[3]:


df_emp = pd.DataFrame(emp) # created dataframe from a dictionary
df_emp


# In[4]:


type(df_emp)


# In[5]:


# access the particular column data : two ways
# 1. we will be using this method.
df_emp['name'] 


# In[6]:


# 2. 
df_emp.name


# In[7]:


# to get the info of each column 1.
df_emp.info()


# In[8]:


# to get the info of each column 2.
df_emp.describe() 


# In[9]:


type(df_emp['name'])


# In[10]:


# access rows : two methods = iloc & loc
# integer location & labelled location
# iloc = to get the particular location
df_emp.iloc[0] # give the first row


# In[11]:


# pass the index number row, column
df_emp.iloc[0,2]


# In[12]:


df_emp.iloc[1:3,2] # we can pass the range


# In[13]:


# we can pass the list : specific rows/columns
df_emp.iloc[[0,2],[0,2]]


# In[14]:


# loc = labelled based
df_emp


# In[15]:


df_emp.loc[1,'name']


# In[16]:


df_emp.loc[1,['name','email']]


# In[17]:


df_emp.loc[0:2,['name','email']]


# In[18]:


df_emp.loc[0:2,'name':'email']


# In[19]:


# set_index method will set the given value as index
# it won't be applied on the original dataframe 
df_emp.set_index('email')


# In[20]:


# if you wanna change the dataframe as per the result then pass the inplace = true
df_emp.set_index('email',inplace = True)


# In[21]:


df_emp


# In[22]:


# access the elements by index 
df_emp.loc['ankit@gmail.com','name':'gender']


# In[23]:


df_emp.loc['ankit@gmail.com':'priya@gmail.com','name':'gender']


# In[24]:


# to reset the index as before
df_emp.reset_index(inplace=True)


# In[25]:


df_emp


# In[26]:


# sorting the index 
df_emp.sort_index() # by default ascending is true


# In[27]:


df_emp.set_index('email',inplace = True)


# In[28]:


df_emp.sort_index(ascending =False) # descend the order


# In[29]:


df_emp.reset_index(inplace=True)


# In[30]:


df_emp['gender']=='Male'


# In[34]:


fc = (df_emp['gender']=='Male')
fc


# In[35]:


# df_emp[(df_emp['gender']=='Male')] #or
df_emp[fc]


# In[41]:


# reverse the condition
fci = ~(df_emp['gender']=='Male')
fci


# In[42]:


df_emp[fci]


# In[40]:


# or with not equals to
fcn = (df_emp['gender'] !='Male')
fcn


# In[43]:


df_emp[fcn]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




