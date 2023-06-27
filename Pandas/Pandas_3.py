#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas_3 = Aggregate functions(sum,min,max,avg), grouping the data, merge or join the data


# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/orders.txt')
df


# In[4]:


df.head()


# In[5]:


df['sales'] # the moment i choose one column it becomes series.


# In[6]:


df['sales'].sum()


# In[7]:


df['sales'].min()


# In[8]:


df['sales'].max()


# In[9]:


df['sales'].mean()


# In[10]:


fc = df['category']== 'Furniture'
df[fc].sum()


# In[11]:


df[fc]['sales'].sum()


# In[12]:


df_cat_sales = df.groupby('category')['sales'].sum()


# In[13]:


df_cat_sales


# In[14]:


df_cat_sales.values


# In[15]:


df_cat_sales.index


# In[16]:


# convert the above series data into a dataframe
pd.DataFrame({'category':df_cat_sales.index,'sales':df_cat_sales.values})


# In[17]:


# directly get a dataframe 
df.groupby('category', as_index= False)['sales'].sum()


# In[18]:


# group by on two columns
df.groupby(['category','city'], as_index= False)['sales'].sum()


# In[19]:


dfc = df.groupby(['category','city'], as_index= False)['sales'].sum()


# In[20]:


type(dfc)


# In[21]:


dfc1 = df.groupby(['category','city'],)['sales'].sum()


# In[22]:


type(dfc1)


# In[23]:


dfc.index


# In[24]:


dfc1.index


# In[25]:


df.head()


# In[26]:


dfcc = df.groupby('category').agg({'sales':'sum','profit':'sum'})


# In[27]:


dfcc


# In[28]:


# aggregate functions on two or more columns
df.groupby('category', as_index= False).agg({'sales':'sum','profit':'min'})


# In[39]:


# merge or join the data
dfr = pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/returns.txt')
dfr


# In[34]:


df


# In[40]:


# same as inner join in sql
pd.merge(left=df,right=dfr , left_on= 'order_id', right_on= 'order_id')


# In[41]:


pd.merge(left = df,right= dfr,how= 'inner' ,left_on= 'order_id', right_on= 'order_id')


# In[42]:


pd.merge(left = df,right= dfr,how= 'left' ,left_on= 'order_id', right_on= 'order_id')


# In[43]:


pd.merge(left = df,right= dfr,how= 'right' ,left_on= 'order_id', right_on= 'order_id')


# In[44]:


pd.merge(left = df,right= dfr,how= 'outer' ,left_on= 'order_id', right_on= 'order_id')


# In[45]:


# if join on multiple columns then pass multiple columns in list
#pd.merge(left = df,right= dfr,how= 'right' ,left_on= ['order_id','another column'], right_on= ['order_id','another column'])


# In[46]:


pd.merge(left = df,right= dfr,how= 'cross')


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




