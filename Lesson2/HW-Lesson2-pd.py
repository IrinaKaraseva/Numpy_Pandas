#!/usr/bin/env python
# coding: utf-8

# #### Работа с данными в Pandas

# In[1]:


import pandas as pd


# In[3]:


authors = pd.DataFrame({'author_id': [1, 2, 3], 'author_name': ['Тургенев', 'Чехов', 'Островский']}, 
                       columns = ['author_id', 'author_name'])


# In[4]:


authors


# In[5]:


book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                    'price': [450, 300, 350, 500, 450, 370, 290]}, columns = ['author_id', 'book_title', 'price'])


# In[6]:


book


# In[22]:


# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
authors_price = pd.merge(authors, book, on = 'author_id')
authors_price


# In[25]:


# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
top5 = authors_price.nlargest(5, 'price')
top5


# In[26]:


# Создайте датафрейм authors_stat на основе информации из authors_price. 
# В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.


# In[34]:


authors_stat = pd.DataFrame({'author_name': authors_price['author_name'].unique(), 
                             'min_price': authors_price.groupby('author_name')['price'].min(),
                            'max_price': authors_price.groupby('author_name')['price'].max(),
                            'mean_price': authors_price.groupby('author_name')['price'].mean()})


# In[35]:


authors_stat


# In[ ]:




