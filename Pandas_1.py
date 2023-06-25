#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# read_csv method in pandas dataframe :syntax: pd.read.csv('path of file' , delimiter = ';')
# it will take comma as delimiter by default in case of comma :pd.read.csv('path of file'), otherwise mention the delimiter.
df = pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/orders.txt')
df


# In[3]:


#top n rows: df.head(n)
df.head() # by default : it shows top 5  if we don't pass n.


# In[4]:


#bottom n rows: df.tail(n)
df.tail() # by default : it shows bottom 5  if we don't pass n.


# In[5]:


# access a column
df['order_id']


# In[6]:


# access multiple columns 
col = ['order_id','category','sales']
df[col]


# In[7]:


df.iloc[2:6,1:3]


# In[8]:


df.loc[2:6,['city','sales']]


# In[9]:


df


# In[10]:


#to check the unique values in any column
df['category'].unique()


# In[11]:


# to count all the values 
df['category'].value_counts()


# In[12]:


df['city'].value_counts() # by default descending order


# In[13]:


df[['category','city']].value_counts()


# In[14]:


pd.options.display.max_rows=100


# In[15]:


df


# In[16]:


fc = (df.category == 'Furniture')
fc


# In[17]:


df[fc]


# In[18]:


fcm = (df.category == 'Furniture') & (df.sales >= 500)
fcm


# In[19]:


fcm = (df.category == 'Furniture') & (df.sales >= 2000)
df[fcm]
df_furniture = df[fcm]


# In[20]:


# to view whole the data set
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)


# In[21]:


df


# In[22]:


# it will create thecsv file of the command and save in your working folder in the system
df_furniture.to_csv('orders_furniture.csv')


# In[23]:


# or condition  (|) = two ways
# 1
fco = (df.category == 'Furniture') | (df.category == 'Technology')
df[fco]


# In[24]:


# or condition  (|) = two ways
# 2 
cat = ['Furniture','Technology']
fcr = df['category'].isin(cat)
df[fcr]


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




