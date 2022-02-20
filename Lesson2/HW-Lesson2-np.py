#!/usr/bin/env python
# coding: utf-8

# #### Вычисления с помощью Numpy

# In[1]:


import numpy as np


# In[18]:


a = np.array([[1, 6],
             [2, 8],
             [3, 11],
             [3, 10],
             [1, 7]])


# In[19]:


a


# In[27]:


mean_a = a.mean(axis = 0)


# In[21]:


# np.save('mean_a', a)


# In[28]:


mean_a


# In[30]:


a_centered = a - mean_a


# In[31]:


a_centered


# In[38]:


b1 = a_centered[0:, 0]
b1


# In[42]:


b2 = a_centered[0:, 1]
b2


# In[47]:


a_centered_sp = np.dot(b1, b2)
a_centered_sp


# In[50]:


# число наблюдений = 5
N = 5
a_centered_sp / (N - 1)

