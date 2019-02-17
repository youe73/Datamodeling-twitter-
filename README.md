# Datamodeling-twitter-

Twitter assignment:

#How many Twitter users are in the database?
db.twitter3.count_documents({})
1599982


#Who are the most mentioned Twitter users? (Provide the top five.)
ppall(db.twitter3.aggregate([  
    {"$group": {"_id": {"user": "$user"},"tweed": {"$addToSet": "$user"},"count": {"$sum": 1}}},
    {"$sort": { "count": -1}},
    { "$limit" : 5 }
],  
    allowDiskUse=True  
))
{'_id': {'user': 'lost_dog'}, 'count': 549, 'tweed': ['lost_dog']}
{'_id': {'user': 'webwoke'}, 'count': 345, 'tweed': ['webwoke']}
{'_id': {'user': 'tweetpet'}, 'count': 310, 'tweed': ['tweetpet']}
{'_id': {'user': 'SallytheShizzle'}, 'count': 281, 'tweed': ['SallytheShizzle']}
{'_id': {'user': 'VioletsCRUK'}, 'count': 279, 'tweed': ['VioletsCRUK']}



#Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?
ppall(db.twitter3.aggregate([
    {"$match":{"polarity":"4"}},
    {"$group": {"_id":{"user":"$user"}, "Positive":{"$push":"$user"}}},
    {"$sort": {"count":-1}},
    {"$limit":5}
    ],  
    allowDiskUse=True 
))
{'Positive': ['millerslab'], '_id': {'user': 'millerslab'}}
{'Positive': ['adbillingsley'], '_id': {'user': 'adbillingsley'}}
{'Positive': ['serianna'], '_id': {'user': 'serianna'}}
{'Positive': ['puchal_ek'], '_id': {'user': 'puchal_ek'}}
{'Positive': ['Kristah_Diggs'], '_id': {'user': 'Kristah_Diggs'}}


#Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?
ppall(db.twitter3.aggregate([
    {"$match":{"polarity":"0"}},
    {"$group": {"_id":{"user":"$user"}, "Negative":{"$push":"$user"}}},
    {"$sort": {"count":-1}},
    {"$limit":5}
    ],  
    allowDiskUse=True 
))
{'Negative': ['dailygluttony'], '_id': {'user': 'dailygluttony'}}
{'Negative': ['alyssa_f17'], '_id': {'user': 'alyssa_f17'}}
{'Negative': ['mattfca'], '_id': {'user': 'mattfca'}}
{'Negative': ['tpchandler'], '_id': {'user': 'tpchandler'}}
{'Negative': ['catfuel'], '_id': {'user': 'catfuel'}}



#Which Twitter users link the most to other Twitter users? (Provide the top ten.)
ppall(db.twitter3.aggregate([
    {"$match":{"text":{"$regex":"@\w+"}}},
    {"$group":{"_id":{"user":"$user"}, "text": {"$addToSet":"$user"},"counted": {"$sum": 1}}},
    {"$sort": { "counted": -1}},
    {"$limit":10 }
    ],
allowDiskUse=True
))
{'_id': {'user': 'lost_dog'}, 'counted': 549, 'text': ['lost_dog']}
{'_id': {'user': 'tweetpet'}, 'counted': 310, 'text': ['tweetpet']}
{'_id': {'user': 'VioletsCRUK'}, 'counted': 251, 'text': ['VioletsCRUK']}
{'_id': {'user': 'what_bugs_u'}, 'counted': 246, 'text': ['what_bugs_u']}
{'_id': {'user': 'tsarnick'}, 'counted': 245, 'text': ['tsarnick']}
{'_id': {'user': 'SallytheShizzle'},
 'counted': 229,
 'text': ['SallytheShizzle']}
{'_id': {'user': 'mcraddictal'}, 'counted': 217, 'text': ['mcraddictal']}
{'_id': {'user': 'Karen230683'}, 'counted': 216, 'text': ['Karen230683']}
{'_id': {'user': 'keza34'}, 'counted': 211, 'text': ['keza34']}
{'_id': {'user': 'TraceyHewins'}, 'counted': 202, 'text': ['TraceyHewins']}


#Who are the most mentioned Twitter users? (Provide the top five.)
ppall(db.twitter3.aggregate([ 
    {"$group": {"_id": {"user": "$user"},"Id": {"$addToSet": "$user"},"count": {"$sum": 1}}},
    {"$sort": { "count": -1}},
    { "$limit" : 5 }
],  
    allowDiskUse=True  
))
{'Id': ['lost_dog'], '_id': {'user': 'lost_dog'}, 'count': 549}
{'Id': ['webwoke'], '_id': {'user': 'webwoke'}, 'count': 345}
{'Id': ['tweetpet'], '_id': {'user': 'tweetpet'}, 'count': 310}
{'Id': ['SallytheShizzle'], '_id': {'user': 'SallytheShizzle'}, 'count': 281}
{'Id': ['VioletsCRUK'], '_id': {'user': 'VioletsCRUK'}, 'count': 279}



#Who are the most active Twitter users (top ten)?
ppall(db.twitter3.aggregate([
    {"$match":{"text":{"$regex":"@\w+"}}},
    {"$group":{"_id":{"text":"$text"}, "user": {"$addToSet":"$user"},"Most active": {"$sum": 1}}},
    {"$sort": { "counted": -1}},
    {"$limit":10 }
    ],  
    allowDiskUse=True  
))
{'Most active': 1,
 '_id': {'text': '   bad day.....damn you @311. What kind of ticket sale was '
                 'that.....'},
 'user': ['Marxk']}
{'Most active': 1,
 '_id': {'text': '  &gt;. Bodies from Air France crash have been found  '
                 'http://twurl.nl/dvu8be (via @Paisano )'},
 'user': ['jjx']}
{'Most active': 1,
 '_id': {'text': '   @Lakers!! I love you guyssss! Those rings.. Mmmyeahh! '
                 'Bling blingg'},
 'user': ['glotweets']}
{'Most active': 1,
 '_id': {'text': "   Couldn't bless'd da mic w/ my bra's in music 2day "
                 '@ERiceOnTheBeat @moneybagzfam1st @circustk'},
 'user': ['iflizi']}
{'Most active': 1,
 '_id': {'text': '   @PERFEKTnCHANCE (Chance) is Boo #29'},
 'user': ['MishGoddess']}
{'Most active': 1, '_id': {'text': '   @Beansummer'}, 'user': ['amipi7682']}
{'Most active': 1,
 '_id': {'text': '     @riceuniversiity I know huh @Kouture85 Im bout to '
                 'cry@Ahmier thanks Marco! *muah*'},
 'user': ['ChinoArmani']}
{'Most active': 1,
 '_id': {'text': '       Hardest working chica i know( mii boss lady) '
                 '@MoneyAceweather (look up to her seriously) lOl'},
 'user': ['mtiishaw']}
{'Most active': 1,
 '_id': {'text': "    I just cut my beard off. It's only been growing for well "
                 "over a year. I'm gonna start it over. @shaunamanu is happy "
                 'in the meantime.'},
 'user': ['MailmanChris']}
{'Most active': 1,
 '_id': {'text': '   @Standing_Stones  Thank you very much for the DVD '
                 'suggestion!  Very nice of you!  Looks good.'},
 'user': ['sinzero66']}



Modelling assignment

Arrays of ancestors
Atomicity
Atomicity is crucial for writing in documents, especially in concurrent environment. It must eliminate the opportunity that some changes occur in time eg. Like when an update in document (array) or a new element being created, it cannot risk that only half of the query have been completed. Its either insert the writing or nothing at all.  MongoDB do not support transactional storing.  

Arrays of ancestors
Indexes
MongoDB creates _id indexes by default, but in cases where it is required to search a large document fast, it is possible to build index in certain fields. Just a trade off is needed between effective search and write operations. As indexes will slow down write and update queries.  

Arrays of ancestors
Large number of collections
MongoDb can easily support large number of collections. One must just consider the overhead of each collection, and _id creation will use 8KB. The searching queries in arrays of ancestors can be done through index, and the performance in read operations will not be affected. The array of ancestors contains the link between the collections through the use of references.

Materialized path
Sharding
Given the increased flexibility in searching (regex/sub-trees) provided by Materialized path, it gains usefulness to search in multiple servers. sharding which is a horizontal scalling distributing its capacity overload in multiple servers benefits in increased capacity, but must sacrifice the simple structure, as the complexity in infrastructure will increase. 

Materialized path
Large number of collections
Materialized path works with strings and regex. For searching it will be more beneficial to provide additional strings to query root/subtrees in order to find the elements without expenses (searching the entire index). For large numbers of collections, the search can be organized so collections can be related in types. This will yield overall good performance without any negative affect. Indexing is also useful in this case as long as it does not exceed the amount of collections.  It uses the reference to search the queries.

Materialized path
Collection contains large number of small documents
MongoDB has the advantage to search in embedded documents, as it can search values within the existing documents. For collections with many small documents, it is meaningful to make a logical grouping where the documents can form relationships to each other. The advantage is that it will reduce the complex queries for searching. In the end it all depends on what kind of documents and size one wants to store in the database. Situations like one-to-one or one-to -many relationships can therefore be done in embedded method, which also will benefit the index.  

Nested sets
Atomicity
An atomic operation performs action in one single document but not the whole operation. In case of nested structuring it could lead to problems as the documents in the subtrees will not be updated.  


Nested sets
Sharding
Deeply nested sets can be effective in searching but can be problematic if the tree structure has to change. The positional identification number to left and right must be restructured if any changes occur. Hence it is most suited for static trees. In case of sharding it requires much planning and consideration regarding storage capacity, collection size, shard key, routing process must be taken into account. A trade off must be made to ensure the best optimal balance. 


Nested sets
Indexes
Indexing can yield an improved effectivity performance. But it still leads to a consideration of Trade off between write and read operation. Inserting/writing to tree structure is will take time and it will depends on what field one wants to index. 

