
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})


# In[4]:


c = r.content 


# In[5]:


c


# In[6]:


soup = BeautifulSoup(c,"html.parser")


# In[11]:


all = soup.find_all("div",{"class":"cities"})


# In[12]:


all


# In[15]:


for item in all:
    print(item.find_all('h2')[0].text)

