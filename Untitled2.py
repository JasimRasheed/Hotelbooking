#!/usr/bin/env python
# coding: utf-8

# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm
import sklearn



# In[25]:


df=pd.read_csv('C:\\Users\\jasim\\Desktop\\hotel_bookings.csv')
df.head()


# In[19]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


df = df.drop('company',axis =1)
df = df.drop('agent',axis =1)
df = df.drop('country',axis =1)
df = df.drop('children',axis =1)


# In[6]:


df.isnull().sum()


# In[7]:


null= df.isnull()
sns.heatmap(null,cbar=False,cmap='viridis',yticklabels=False)


# In[8]:


df.hist(bins=50, figsize=(20,15))
plt.tight_layout()
plt.show()


# In[9]:


cor= df.corr()
cor


# In[10]:


sns.heatmap(cor, annot= True)
plt.show()


# In[11]:


sns.countplot(x=df['is_canceled'])


# In[12]:


sns.countplot(x=df['arrival_date_month'])


# In[13]:


sns.countplot(x=df['lead_time'],order=(df['lead_time'].value_counts().head(20)).index)
plt.xticks(rotation=90)


# In[14]:


canceled_data = df['is_canceled']
sns.countplot(canceled_data, palette='husl')

plt.show()


# In[15]:


cols = ['Red', 'Blue']
df['is_canceled'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True, colors=cols)


# In[16]:


plt.figure(figsize = (18,8))
sns.set_style("whitegrid")
ax = sns.violinplot(x = 'arrival_date_month', y = 'lead_time' ,data=df)
ax.set_xlabel('Month', fontsize = 20)
ax.set_ylabel('Lead Time', fontsize = 20)
ax.set_title('Most Number of Lead Time', fontsize = 30)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




