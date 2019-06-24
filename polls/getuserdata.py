from .models import User,Tweet,Following,Relationship
from datetime import datetime
from itertools import chain

def getTweets(user_attributes):
  if(len(user_attributes)):
          #print(user_attributes[0]['screenname'])
          tweets = Tweet.objects.filter(user=user_attributes[0]['user_id'])
          tweetordered = tweets.order_by('createdat')
          return tweetordered.values()
  else:
    return []

def getDate(tweets):
  if len(tweets)>0:
            borndate = tweets[0]['createdat']
            d0 = datetime.now().date()
            age = d0 - borndate
            years = age.days//365
            if years>0:
              age = str(years) + " years old"
            else:
              age = str(age.days//30 + 1) + " months old"
  else: 
            age = "0 days"
  return age

def getDates(user_attributes):
  if(len(user_attributes)>0):
    #relationships = Relationship.objects.filter(user1_id = user_attributes[0]['user_id'],typeofrelationship='Single') | Relationship.objects.filter(user2_id = user_attributes[0]['user_id'],typeofrelationship='Signle') 
    relationshipsuser1 = Relationship.objects.filter(user1_id = user_attributes[0]['user_id'],typeofrelationship='Date').values()
    relationshipsuser2 = Relationship.objects.filter(user2_id = user_attributes[0]['user_id'],typeofrelationship='Date').values()
    user1relationships = []
    if(len(relationshipsuser1)>0):
      for relationship in relationshipsuser1:
        userrelationship = User.objects.filter(user_id = relationship['user2_id']).values()
        user1relationships.append(userrelationship[0])
    if(len(relationshipsuser2)>0):
      for relationship in relationshipsuser2:
        userrelationship = User.objects.filter(user_id = relationship['user1_id']).values()
        user1relationships.append(userrelationship[0])
    result = list(chain(relationshipsuser1,relationshipsuser2))
    return user1relationships
  else:
    return []

def getMarrige(user_attributes):
  if(len(user_attributes)>0):
    #relationships = Relationship.objects.filter(user1_id = user_attributes[0]['user_id'],typeofrelationship='Single') | Relationship.objects.filter(user2_id = user_attributes[0]['user_id'],typeofrelationship='Signle') 
    relationshipsuser1 = Relationship.objects.filter(user1_id = user_attributes[0]['user_id'],typeofrelationship='Married').values()
    relationshipsuser2 = Relationship.objects.filter(user2_id = user_attributes[0]['user_id'],typeofrelationship='Married').values()
    userrelationships = []
    if(len(relationshipsuser1)>0):
      for relationship in relationshipsuser1:
        userrelationship = User.objects.filter(user_id = relationship['user2_id']).values()
        userrelationships.append(userrelationship[0])
    if(len(relationshipsuser2)>0):
      for relationship in relationshipsuser2:
        userrelationship = User.objects.filter(user_id = relationship['user1_id']).values()
        userrelationships.append(userrelationship[0])
    result = list(chain(relationshipsuser1,relationshipsuser2))
    return userrelationships
  else:
    return []

def getFans(user_attributes):
  user_id = user_attributes[0]['user_id']
          #followers = Following.objects.filter(user=user_id).values()
  followers = Following.objects.filter(user_id = user_id).values()
  fans = []
  for follower in followers:
     newuser = User.objects.filter(user_id = follower['follower_id']).values()
     fans.append(newuser[0])
  return fans