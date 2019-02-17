
# coding: utf-8

# In[1]:


import csv
import json

csvfile = open('training.1600000.processed.noemoticon.csv', 'r')
jsonfile = open('twitteranalysis.json', 'w')


# In[2]:


fieldnames = ("polarity","id","date","query","user","text")
reader = csv.DictReader(csvfile, fieldnames)

entries =[]
for row in reader:
    if row:
        #print(row)            
        json.dump(row, jsonfile)
        jsonfile.write('\n')


# In[3]:


import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.myDB
twitter3 = db.twitter3
print("Database created")


# In[4]:


#db.twitter2.delete_many({})
db.twitter3.count_documents({})


# In[5]:


from bson.json_util import loads
count = 0
file = open('twitteranalysis.json','r')
for y in file:
    data = json.loads(y)
    #print(data)
    #db.twitter3.insert_one(data)
    count = count +1
db.twitter3.count_documents({})


# In[6]:


#How many Twitter users are in the database?
db.twitter3.count_documents({})


# In[7]:


import pprint

def pp(obj):
    pprint.pprint(obj)
    
def ppall(col):
    for p in col:
        pp( p )


# In[12]:


#Who are the most mentioned Twitter users? (Provide the top five.)
ppall(db.twitter3.aggregate([  
    {"$group": {"_id": {"user": "$user"},"tweed": {"$addToSet": "$user"},"count": {"$sum": 1}}},
    {"$sort": { "count": -1}},
    { "$limit" : 5 }
],  
    allowDiskUse=True  
))


# In[ ]:


#How many Twitter users are in the database? done
#Who are the most active Twitter users (top ten)?
#Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)? done
#Which Twitter users link the most to other Twitter users? (Provide the top ten.) - most appearing @ tweeds
#Who are the most mentioned Twitter users? (Provide the top five.) - count usernames


# In[13]:


#Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?
ppall(db.twitter3.aggregate([
    {"$match":{"polarity":"4"}},
    {"$group": {"_id":{"user":"$user"}, "Positive":{"$push":"$user"}}},
    {"$sort": {"count":-1}},
    {"$limit":5}
    ],  
    allowDiskUse=True 
))


# In[14]:


#Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?
ppall(db.twitter3.aggregate([
    {"$match":{"polarity":"0"}},
    {"$group": {"_id":{"user":"$user"}, "Negative":{"$push":"$user"}}},
    {"$sort": {"count":-1}},
    {"$limit":5}
    ],  
    allowDiskUse=True 
))


# In[18]:


#Which Twitter users link the most to other Twitter users? (Provide the top ten.)
ppall(db.twitter3.aggregate([
    {"$match":{"text":{"$regex":"@\w+"}}},
    {"$group":{"_id":{"user":"$user"}, "text": {"$addToSet":"$user"},"counted": {"$sum": 1}}},
    {"$sort": { "counted": -1}},
    {"$limit":10 }
    ],
allowDiskUse=True
))


# In[84]:





# In[19]:


#Who are the most mentioned Twitter users? (Provide the top five.)
ppall(db.twitter3.aggregate([ 
    {"$group": {"_id": {"user": "$user"},"Id": {"$addToSet": "$user"},"count": {"$sum": 1}}},
    {"$sort": { "count": -1}},
    { "$limit" : 5 }
],  
    allowDiskUse=True  
))


# In[24]:


#Who are the most active Twitter users (top ten)?
ppall(db.twitter3.aggregate([
    {"$match":{"text":{"$regex":"@\w+"}}},
    {"$group":{"_id":{"text":"$text"}, "user": {"$addToSet":"$user"},"Most active": {"$sum": 1}}},
    {"$sort": { "counted": -1}},
    {"$limit":10 }
    ],  
    allowDiskUse=True  
))

