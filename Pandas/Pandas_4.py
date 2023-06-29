#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas time series, type casting, working with other file types,plot graphs, pivot_table


# In[2]:


import pandas as pd
df = pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/orders.txt')
df


# In[3]:


df.dtypes # in this order date's type as object to change that as date we use parse_dates


# In[4]:


df = pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/orders.txt', parse_dates=['order_date'])
df


# In[5]:


df.dtypes # now  order date's type as object changed to datetime64 


# In[6]:


# another method of changing any date column to datetime is
#pd.to_datetime(df['order_date'])


# In[7]:


dates = ['2020-01-01','2021-04-05']
type(dates)


# In[8]:


pd.to_datetime(dates)


# In[9]:


# if your date is in another format for that:
datess = ['2020$01$01','2021$04$05']
pd.to_datetime(datess, format= '%Y$%m$%d')


# In[10]:


# if mixed format are present in dataset
dates = {'Dates':['3/14/2020','2021-08-03']}
df = pd.DataFrame(dates)
df


# In[11]:


print(pd. __version__)


# In[12]:


pd.to_datetime(df['Dates'], format= 'mixed')


# In[13]:


dates = ['2020/01/15','2021-01-15']
pd.to_datetime(dates, format= 'mixed')


# In[14]:


df = pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/orders.txt', parse_dates=['order_date'], index_col='order_date')
df


# In[15]:


df.loc['2018']


# In[16]:


# slicing with date index
df['2018-03-01':'2019-05-02']


# In[17]:


df.sort_index()


# In[18]:


df.reset_index(inplace = True)


# In[19]:


df


# In[20]:


df.dtypes


# In[21]:


df['order_year'] = df['order_date'].dt.year


# In[22]:


df


# In[23]:


df['order_date'].dt.month


# In[24]:


df['order_date'].dt.day_name()


# In[25]:


df['order_date'].dt.weekday


# In[26]:


import matplotlib
import matplotlib_inline
#pip install matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


df


# In[28]:


df.plot('category','sales')


# In[29]:


df.plot('category','sales', kind = 'bar')


# In[30]:


df = pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/orders.txt', parse_dates=['order_date'], index_col='order_date')
df


# In[31]:


# Plotting methods allow for a handful of plot styles other than the default line plot.
#These methods can be provided as the kind keyword argument to plot(), and include:
# ‘bar’ or ‘barh’ for bar plots

# ‘hist’ for histogram

# ‘box’ for boxplot
# ‘kde’ or ‘density’ for density plots

# ‘area’ for area plots

# ‘scatter’ for scatter plots

# ‘hexbin’ for hexagonal bin plots

# ‘pie’ for pie plots


# In[32]:


df['sales'].plot(kind = 'hist') # takes index (order_date) as x axis a


# In[33]:


df['sales'].plot(kind = 'line')


# In[34]:


df.groupby('category')['sales'].sum().plot()


# In[35]:


df


# In[36]:


# monthwise mean
df['sales'].resample('M').mean()


# In[37]:


#  monthwise sum
df['sales'].resample('M').sum()


# In[38]:


# quarterwise sum
df['sales'].resample('Q').sum().plot(kind = 'bar')


# In[39]:


df['sales'].resample('Y').sum().plot(title= "sales")


# In[40]:


df.dtypes


# In[41]:


df['sales'].astype('int')


# In[42]:


# if we have null value or NaN value in any column then we cant convert the dtype to another
# first we fill the null with 0 or something then change the type
# df['sales'].fillna(0).astype('int')


# In[43]:


df.pivot_table(index='city', columns= 'category', values= 'sales')


# In[44]:


df.pivot_table(index='city', columns= 'category', values= 'sales', aggfunc='sum')


# In[45]:


df1=pd.read_excel('C:/Users/MY DEVICE/Downloads/all_excel_files/Artist_DataSet.xlsx')


# In[46]:


df1


# In[47]:


df2=pd.read_excel('C:/Users/MY DEVICE/Downloads/Final_Project Dataset Alex.xlsx')


# In[48]:


df2


# In[49]:


df2=pd.read_excel('C:/Users/MY DEVICE/Downloads/Final_Project Dataset Alex.xlsx',sheet_name= 'Working_sheet')
df2


# In[50]:


# install openpyxl
# can give sheet names or index to access other sheets in same excel.
df2=pd.read_excel('C:/Users/MY DEVICE/Downloads/Final_Project Dataset Alex.xlsx',sheet_name= 0)
df2


# In[52]:


df


# In[61]:


df=  pd.read_csv('C:/Users/MY DEVICE/Downloads/ankit python assign/returns.txt')
df


# In[60]:


#to_excel : can convert any dataframe to excel
df.to_excel('C:/Users/MY DEVICE/Downloads/ankit python assign/orders1.xlsx', sheet_name="orders")


# In[62]:


#to_json
df.to_json('C:/Users/MY DEVICE/Downloads/ankit python assign/returnsjson.json')


# In[63]:


df_json = pd.read_json('C:/Users/MY DEVICE/Downloads/ankit python assign/returnsjson.json')


# In[64]:


df_json


# In[67]:


#to_parquet : secured coz its compressed , takes less space, fast performance. 
df.to_parquet('C:/Users/MY DEVICE/Downloads/ankit python assign/returns_p.parquet')


# In[68]:


df_par = pd.read_parquet('C:/Users/MY DEVICE/Downloads/ankit python assign/returns_p.parquet')
df_par


# In[ ]:




