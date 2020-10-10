#!/usr/bin/env python
# coding: utf-8

#  
# <h2> Capstone Project - Car accident severity (Week 1)</h2>
#  

# <h4>Introduction/Business Problem</h4>
# Severity of accidents in Seattle city is the Data set.
# The project is to predict the severity of an accident based on the independent variables.

# <h4>Data section</h4>
# 
# Severity of accidents in Seattle city is the Data set.The Data set has 194673 rows and 38 columns. SEVERITYCODE is the Dependent variable. Independent variables used are:-
# 1.COLLISIONTYPE: Describes the type of crash.
# 2.WEATHER: Describes the weather at the time of crash. 
# 3.ROADCOND: Describes the condition of the road at the time of crash.
# 4.LIGHTCOND: Describes the light conditions at the time of crash.
# 5.INATTENTIONIND: Describes whether the driver was distracted
# 6.UNDERINFL: Describes whether the driver was under the influence.

# In[14]:


import pandas as pd
df=pd.read_csv('Data-Collisions.csv')
df=df[['COLLISIONTYPE','WEATHER','ROADCOND','LIGHTCOND','INATTENTIONIND','UNDERINFL','SEVERITYCODE']]
df.head()


# In[10]:


df['SEVERITYCODE'].value_counts().plot(kind='bar')


# In[11]:


df['WEATHER'].value_counts().plot(kind='bar')


# In[ ]:




