#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas_3_1 = union,# restore the old index,drop duplicates,# row and columnwise drop NaN, fill the value at NaN,read_clipboard


# In[2]:


import pandas as pd
emp= {"name":["Ankit","Rahul","Priya"],"gender":["Male","Male","Female"], "email":["ankit@gmail.com","rahul@gmail.com","priya@gmail.com"] }
df1 = pd.DataFrame(emp)
df1


# In[3]:


emp= {"name":["Pankaj","Sumit"],"gender":["Male","Male"], "email":["Pankaj@gmail.com","Sumit@gmail.com"] }
df2 = pd.DataFrame(emp)
df2


# In[4]:


# Union = number of columns of both dataframs should be same
pd.concat([df1,df2])


# In[5]:


# created new index
df=pd.concat([df1,df2], ignore_index=True)
df


# In[6]:


# restore the old index
pd.concat([df1,df2]).reset_index()


# In[7]:


# drop duplicates
df


# In[8]:


emp1= {"name":["Ankit","Priya"],"gender":["Male","Female"], "email":["ankit@gmail.com","priya@gmail.com"] }
df11 = pd.DataFrame(emp1)
df11


# In[9]:


df0=pd.concat([df,df11], ignore_index=True)
df0


# In[10]:


# drop duplicates
df.drop_duplicates()


# In[11]:


emp11= {"name":["Ankita","Riya"],"gender":["Male","Female"], "email":["ankit@gmail.com","priya@gmail.com"] }
df111 = pd.DataFrame(emp11)
df111


# In[12]:


df01=pd.concat([df,df111], ignore_index=True)
df01


# In[13]:


# drop the duplicate from particular column
df01.drop_duplicates(subset= 'email')


# In[14]:


df01.drop_duplicates(subset= 'email' , keep = 'first')


# In[15]:


df01.drop_duplicates(subset= ['email','gender'] , keep = 'last')


# In[16]:


df01.drop_duplicates(subset= ['email','gender'] , keep = False)


# In[17]:


df01


# In[18]:


dff =  df01.groupby('email')['name'].count()
dff


# In[41]:


import numpy as np
emp22= {"name":[np.nan,"Deepak", "Ankita","Riya"],"gender":[np.nan,"Male",np.nan,"Female"], "email":[np.nan,"deepak@gmail.com","ankita@gmail.com",np.nan] }
df112 = pd.DataFrame(emp22)
df112


# In[42]:


df112.isna()


# In[43]:


df112['gender'].isna()


# In[44]:


df112[df112['gender'] == 'Male']


# In[45]:


df112.dropna() # drop all the rows that contains NaN 


# In[46]:


df112


# In[47]:


df112.dropna(how = 'any')


# In[48]:


df112.dropna(how = 'all') # drop all the rows that contains all NaN


# In[49]:


# columnwise drop NaN
df112.dropna(how = 'any', axis = 'columns') # all the columns has NaN = empty dataset


# In[50]:


empe= {"name":["Rahul","Deepak", "Ankita","Riya"],"gender":[np.nan,"Male",np.nan,"Female"], "email":[np.nan,"deepak@gmail.com","ankita@gmail.com",np.nan] }
dfe = pd.DataFrame(empe)
dfe


# In[51]:


# columnwise drop NaN
dfe.dropna(how = 'any', axis = 'columns') # only name column has all values


# In[52]:


dfe.dropna(how = 'any', axis = 'index') # by default its index


# In[53]:


dfe.dropna(subset=['name','email'], how = 'any', axis = 'index') # mentioned columns dont have NaN


# In[54]:


dfe


# In[55]:


dfe['gender'].fillna(value = 'new') # where is NaN it will fill the value


# In[57]:


dfe['gender'].fillna(value = 'new', inplace= True)# inplace= True; CHANGE THE VALUE IN ORIGINAL data
dfe


# In[58]:


dfclip = pd.read_clipboard(sep=' ') # copy the data then mention the value it is separated by like comma or space
dfclip


# In[ ]:





# In[ ]:




