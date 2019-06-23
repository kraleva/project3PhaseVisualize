from .models import User,Tweet,Following
from datetime import datetime

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


def getFans(user_attributes):
  user_id = user_attributes[0]['user_id']
          #followers = Following.objects.filter(user=user_id).values()
  followers = Following.objects.filter(user_id = user_id).values()
  fans = []
  for follower in followers:
     newuser = User.objects.filter(user_id = follower['follower_id']).values()
     fans.append(newuser[0])
  return fans