
# coding: utf-8

# In[44]:


import requests, pandas
from bs4 import BeautifulSoup

dic_list = []

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s=0"
init_req = requests.get(base_url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
page_soup = BeautifulSoup(init_req.content, "html.parser")
page_num = int(page_soup.find_all("a",{"class":"Page"})[-1].text)

for page in range(0,page_num*10,10):
    url = base_url + str(page)
    r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    soup = BeautifulSoup(r.content, "html.parser");
    allProperties = soup.find_all("div",{"class":"propertyRow"})
    for item in allProperties:
        dic = {}
        dic["Price"] = item.find("h4",{"class":"propPrice"}).text.replace('\n','').replace(' ','')
        dic["Address"] = item.find_all("span",{"class":"propAddressCollapse"})[0].text
        dic["Locality"] = item.find_all("span",{"class":"propAddressCollapse"})[1].text
        try:
            dic["Beds"] = item.find("span",{"class":"infoBed"}).text
        except:
            dic["Beds"] = None
        try:
            dic["Area"] = item.find("span",{"class":"infosqft"}).text
        except:
            dic["Area"] = None
        try:
            dic["Full Baths"] = item.find("span",{"class":"infoValueFullBath"}).text
        except:
            dic["Full Baths"] = None
        try:
            dic["Half Baths"] = item.find("span",{"class":"infoValueHalfBath"}).text
        except:
            dic["Half Baths"] = None

        for column_group in item.find_all("div",{"class","columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class","featureGroup"}),column_group.find_all("span",{"class","featureName"})):
                if "Lot Size" in feature_group.text:
                    dic["Lot Size"] = feature_name.text
                
        dic_list.append(dic)
        print("")

df = pandas.DataFrame(dic_list)
print(df)


# In[38]:


df


# In[34]:


df.to_csv('Output.csv')


# In[45]:


df

