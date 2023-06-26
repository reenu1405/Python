#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In Pandas_1 we have covered : Pandas, Dataframe , how to create , slicing via loc & iloc , filter data


# In[58]:


# In this pandas_2 = filter, update, drop ,sort


# In[2]:


emp = {'name' : 'Ankit','gender':'Male','email':'ankit@gmail.com'}
emp = {'name' : ['Ankit','Rahul','Priya'],'gender':['Male','Male','Female'],'email':['ankit@gmail.com','rahul@gmail.com','priya@gmail.com']}
emp


# In[3]:


import pandas as pd


# In[4]:


df = pd.DataFrame(emp) # created dataframe from a dictionary
df


# In[5]:


# filter
fc = (df['name']=='Ankit')
df.loc[0]


# In[6]:


df.loc[fc]


# In[7]:


df.loc[fc,'gender']


# In[8]:


df.index


# In[9]:


# # override the index
# df.index = ['a','b','c']
# df


# In[10]:


# df.index = ['0','1','2']
# df


# In[11]:


df


# In[12]:


#df[fc,'gender']
df.loc[fc,['gender']]


# In[13]:


df.columns


# In[14]:


# assign name or rename the columns 
df.columns = ['emp_name','gender','emp_email']
df


# In[15]:


df.rename(columns={'emp_name':'name','emp_email':'email'})


# In[16]:


# change or update the values
df.loc[0] = ['Ankitt','Male','ankitt@gmail.com']
df


# In[17]:


# reset the previous column names
df.columns = ['name','gender','email']
df


# In[18]:


# change the values with column name
df.loc[0,['name','email']] = ['Ankit','ankit@gmail.com']


# In[19]:


df


# In[20]:


#filter the data
fc = (df['gender']=='Male')
df.loc[fc]


# In[21]:


# update the data with filter
df.loc[fc,'gender'] ='Female' # all the values where gender = male, will be updated as Female


# In[22]:


df


# In[23]:


# update whole column
df.loc[:,'gender'] ='Male' # loc
# df.loc[:,1] ='Male' # iloc


# In[24]:


df


# In[25]:


fc = (df['name']=='Priya')
df.loc[fc,'gender']='Female'


# In[26]:


df


# In[27]:


# length of each name
df['name'].apply(len)


# In[28]:


def update_email(email):
    return email.upper()


# In[29]:


df['email'].apply(update_email) # apply :apply the update_email function only on email column


# In[30]:


df


# In[31]:


df.applymap(update_email)  # applymap = we didnt mention any column name here so the update_email method applied on whole df


# In[32]:


df['name'].str.upper() # applying string functions : first convert it to string with .str then use the function


# In[33]:


df


# In[34]:


df['name'].str.contains('a')


# In[36]:


df['name'].str.startswith('A')


# In[37]:


df


# In[38]:


df['salary'] = 10000


# In[39]:


df


# In[40]:


df['name_gender'] = df['name']+ ' '+ df['gender']


# In[41]:


df


# In[42]:


fc = df['name'] == 'Ankit'
df.loc[fc,'salary'] = 5000


# In[43]:


df


# In[44]:


# drop a column
# df.drop(index = 0,inplace = True)
df.drop(index = 0) # its not on original df , to change original dataframe with the function pass inplace = True


# In[45]:


df


# In[46]:


fc = df['salary']>5000
fc


# In[47]:


# delete the data which satisfies the above condition
df.drop(index= df[fc].index)


# In[48]:


df[fc].index


# In[49]:


# delete a column
df.drop(columns=['name_gender'])


# In[50]:


# sort the data
df.sort_values(by='name') # sorting in ascending 


# In[51]:


df.sort_values(by='name' ,ascending= False ) # sorting in descending 


# In[52]:


df.sort_values(by=['gender','salary']) 


# In[54]:


df.sort_values(by=['gender','salary'],ascending= [False,True]) 


# In[57]:


In[20]

