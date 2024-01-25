#!/usr/bin/env python
# coding: utf-8

# # Yitu  data science 
# **basic for data science**
# *using python! enjoy*

# In[10]:


x=1983
print(x)


# # Import liberaris

# In[12]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[14]:


# import csv file
df = pd.read_csv('Sales Data.csv', encoding= 'unicode_escape')


# In[16]:


df.head()


# In[20]:


df.shape


# In[22]:


df.info()


# In[23]:


#drop unrelated/blank columns

df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[24]:


#check for null values

pd.isnull(df).sum()


# In[25]:


# drop null values

df.dropna(inplace=True)


# In[26]:


# change data type

df['Amount'] = df['Amount'].astype('int')


# In[27]:


df['Amount'].dtypes


# In[29]:


df.columns


# In[30]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)

df.describe()


# In[31]:


# use describe() for specific columns

df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ### Gender

# In[33]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# #### From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# #### age

# In[35]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# *From above graphs we can see that most of the buyers are of age group between 26-35 yrs female*

# ### state

# In[36]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# *From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*
# 

# ### marital status

# In[37]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[38]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

# ### Occupation 

# In[39]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# *From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*

# ### Product Category 

# In[41]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[42]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# *From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*

# In[43]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[44]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # conclusion 
# *Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*

# In[ ]:





# In[7]:


a=np.array([6,7,8,9,10])
print(a)
print(type(a))


# In[9]:


b=np.array([[1,2,3],[4,5,6]])
print(b)


# In[ ]:





# In[14]:


def getdatafromUser():
    D={}
    while True:
        studentId=input("Enter student Id")
        marklist=input("enter students mark separated by comma")
        morestudents=input("enter yes to add more students")
        if studentId in D:
            print(studentId, "already registered")
        else:
            D[studentId]=marklist.split(",")
        if morestudents.lower()=="no":
            return D


# In[ ]:


studentdata=getdatafromUser()


# In[ ]:


print(studentdata)


# In[ ]:




