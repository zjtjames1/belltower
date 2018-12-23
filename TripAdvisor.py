
# coding: utf-8

# In[4]:


#import all pakages:
import requests
import json
from lxml.html import fromstring


# In[5]:


# titles:
def get_titles_from_urls(url):
    urls = requests.get(url)
    tree = fromstring(urls.text)
    titles = tree.xpath('//span[@class="noQuotes"]')
    return [a.text.strip() for a in titles]


# In[6]:


# reviews:
def get_reviews_from_urls(url):
    urls = requests.get(url)
    tree = fromstring(urls.text)
    reviews = tree.xpath('//p[@class="partial_entry"]')
    return [b.text.strip() for b in reviews]


# In[10]:


def get_locations_from_urls(url):
    urls = requests.get(url)
    tree = fromstring(urls.text)
    try:
        locations = tree.xpath('//span[@class="expand_inline userLocation___111"]')
    except Exception as e:
        pass    
    return [c.text.strip() for c in locations]


# In[11]:


#create functions to retrieve the first 10 pages of reviews for each spot:
#Xián Bell Tower:
allreviews = []
alltitles = []
alllocations = []
i=0
while i <= 9:
    all_pages_BellTower = ['https://www.tripadvisor.com/Attraction_Review-g298557-d1801562-Reviews-or' + str(i) + '0-Xi_an_Bell_Tower-Xi_an_Shaanxi.html']
    i = i + 1
    for page in all_pages_BellTower:
        titles = get_titles_from_urls(page)
        reviews = get_reviews_from_urls(page)
        locations = get_locations_from_urls(page)
        alltitles.extend(titles) 
        allreviews.extend(reviews)
        alllocations.extend(locations)
print(len(alltitles), len(allreviews), len(alllocations))


# In[12]:


#Xián city wall:
all_pages_CityWall = ['https://www.tripadvisor.com/Attraction_Review-g298557-d459901-Reviews-Xi_an_City_Wall_Chengqiang-Xi_an_Shaanxi.html']

