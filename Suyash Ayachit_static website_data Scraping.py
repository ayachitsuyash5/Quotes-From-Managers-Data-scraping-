#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().system(' pip install requests')


# In[38]:


import requests


# In[39]:


from bs4 import BeautifulSoup


# In[40]:


url= 'https://devtomanager.com/interviews/'


# In[41]:


import os


# In[42]:


os.chdir('E:/Scripting')


# In[43]:


html_interview = requests.get(url)
html_interview


# In[44]:


html_interview = requests.get(url).text
html_interview


# In[45]:


soup = BeautifulSoup(html_interview, "html.parser")


# In[46]:


print(soup)


# In[47]:


soup.find_all('title')


# In[48]:


soup.find_all("h5", class_='card-title')


# In[49]:


employee_name = [i.text.strip() for i in soup.find_all('h5',class_='card-title')]
employee_name


# In[50]:


len(employee_name)


# In[51]:


soup.select('div.card-body')[0].find_all('p', class_='card-text')[0].text.strip()


# In[52]:


quotes = [i.find_all('p', class_='card-text')[0].text.strip() for i in soup.select('div.card-body')]
quotes


# In[53]:


tags = []
for r in soup.select('div.card-body'):
    q = r.find_all('strong', class_ ='mr-2')
    tags.append([i.text.strip() for i in q])
tags


# In[54]:


len(tags)


# In[55]:


soup.select('div.card-body')[0].find_all('p', class_ = 'card-text')[1].text.split()[:3]


# In[56]:


dates = []
for r in soup.select('div.card-body'):
    dates.append(r.find_all('p', class_='card-text')[1].text.split()[:3])
dates


# In[57]:


date = []
for d in dates:
    date.append("".join(d))
date


# In[58]:


len(date)


# In[60]:


import pandas as pd
def manager(soup):
    employee_name = [i.text.strip() for i in soup.find_all('h5',class_='card-title')]
    quotes = [i.find_all('p', class_='card-text')[0].text.strip() for i in soup.select('div.card-body')]
    dates = []
    for r in soup.select('div.card-body'):
        dates.append(r.find_all('p', class_='card-text')[1].text.split()[:3])
        date = []
        for d in dates:
            date.append("".join(d))
    tags = []
    for r in soup.select('div.card-body'):
        q = r.find_all('strong', class_ ='mr-2')
        tags.append([i.text.strip() for i in q])
    return pd.DataFrame({"Employee Name and Position":employee_name, "Quotes":quotes,'Date': dates, 'Tags': tags})


# In[61]:


df = manager(soup)


# In[71]:


df 


# In[72]:


df.shape


# In[64]:


stud = 'https://devtomanager.com/interviews/={}' #for scraping 5 pages


# In[65]:


stud.format(5)


# In[66]:


tables=[]
for i in range(1,51):
    url_all = stud.format(i)
    html_all = requests.get(url_all).text
    soup = BeautifulSoup(html_all,'html.parser')
    tables.append(manager(soup))


# In[67]:


tables=[]
from tqdm import tqdm
for i in tqdm(range(1,51)):
    url_all = stud.format(i)
    html_all = requests.get(url_all).text
    soup = BeautifulSoup(html_all,'html.parser')
    tables.append(manager(soup))


# In[70]:


tables


# In[73]:


tables1=[]
from tqdm import tqdm
import time
for i in tqdm(range(1,51)):
    url_all = stud.format(i)
    html_all = requests.get(url_all).text
    time.sleep(5)
    soup = BeautifulSoup(html_all,'html.parser')
    tables.append(manager(soup))


# In[74]:


data = pd.concat(tables,axis=0,ignore_index = True)
data.head()


# In[77]:


df.to_csv("managerquotes.csv")


# In[78]:


df.to_csv()

