#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("employees.csv")
df


# In[3]:


df.shape


# In[4]:


df.head()
df.tail()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[11]:


df[df.duplicated()] 


# In[17]:


df = df.drop_duplicates(keep='first') 
df


df = df.drop_duplicates(keep='last') 
df


# In[18]:


df.shape


# In[23]:


df.corr(numeric_only=True)


# In[27]:


sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='Blues')


# In[29]:


df.columns


# In[30]:


ftr = ['satisfactoryLevel', 'lastEvaluation', 'numberOfProjects',
       'avgMonthlyHours', 'timeSpent.company', 'workAccident',
       'promotionInLast5years', 'dept', 'salary']


# In[31]:


for i,j in enumerate(ftr):                            #returns the index value along with the values present isnide the list
  print(i,j)


# In[44]:


fig=plt.subplots(figsize=(100,70))

for p,q in enumerate(ftr):    #p will print the index value and q will print the column names
    plt.subplot(3,3,p+1)
    plt.subplots_adjust(hspace=0.3)
    sns.countplot(x=q,data=df, hue='left')
    plt.xticks(rotation=90)
    


# # Observations, of where To improve in the Company:
# 
# ### Promotion:Likely quit---> Havent  recieved promotion
# 
# ### Time with Company: After 3 -6 year Crucial point the employee, affection with organisation.
# 
# ### Number of project: if the opportunities are less or if the employee is over burdened , more chance of the employeee to quit the jobs.
# 
# ### Salary : incentives based system to be introduced.

# In[ ]:




