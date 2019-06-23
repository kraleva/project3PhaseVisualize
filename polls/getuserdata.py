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