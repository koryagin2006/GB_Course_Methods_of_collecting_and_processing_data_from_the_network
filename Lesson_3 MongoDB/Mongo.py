from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost',27017)
db = client['database_305']
users = db.users305
# letters = db.letters_305

# users.insert_one({'author':'Second_author',
#                  'age':19,
#                   'tags':'Super tag!'})
#
# users.insert_many([{"author": "Peter",
#                "age" : 56,
#                "text": "Wildberry is cool!",
#                "tags": ['cool','hot','ice'],
#                "date": '28.11.1970'},
#
#                     {"author": "John",
#                "age" : 28,
#                "title": "Hot Cool!!!",
#                "text": "easy too!",
#                "date": '13.03.2015'}])

new_author = {"author": "John 2",
               "age" : 28,
               "title": "Not cool",
               "text": "easy too!",
               "date": '16.03.2019'}


# pprint(users)

# $gt, $lt, $gte, $lte, $eq

# for user in users.find({'age':{'$gt':30}}).sort('author').limit(1):
#     pprint(user)


# users.update_many({'author':'John'},{'$set':new_author})

users.delete_many({'author':['Second_author','Peter']})

for user in users.find():
    pprint(user)



