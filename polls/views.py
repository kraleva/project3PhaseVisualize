from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,Http404
from .models import User,Tweet,Following
from django.db.models import Q
from . forms import NameForm
from django import forms
from datetime import datetime
from . getuserdata import getTweets,getDate, getFans,getDates, getMarrige,getTweet

def index(request):
  if request.method == 'GET':
    query = request.GET.get('screenname')
    form = NameForm(request.GET)
    if query:
      latest_user_list = User.objects.filter(screenname__icontains=str(query))
      context = {
        'latest_user_list':[],
        'searcheduser': latest_user_list,
        'form': form
      }
    else:
      latest_user_list = User.objects.all()
      context = {
        'latest_user_list':latest_user_list,
        'form': form
      }
    return render(request,'polls/index.html',context)

def users(request, user_screenname):
    try:
        query = request.GET.get('screenname')
        form = NameForm(request.GET)
        if query:
          #if do nothing
          latest_user_list = User.objects.filter(screenname=str(query))
          if len(latest_user_list)>0:
            return redirect("http://localhost:8000/"+latest_user_list[0].screenname)
        else:
          user = User.objects.filter(screenname=str(user_screenname))
          user_attributes = user.values()
          tweets = getTweets(user_attributes)
          age = getDate(tweets)
          fans = getFans(user_attributes)
          dates = getDates(user_attributes)
          marriges = getMarrige(user_attributes)
          return render(request, 'polls/user.html', {
          'dates': dates,
          'tweets': tweets,
          'marriges':marriges,
          'user': user_attributes[0],
          'followers': fans,
          'age': age,
          'form': form})
    except User.DoesNotExist:
        raise Http404("Question does not exist")


def tweet(request,user_screenname,tweet_id):
    tweet = getTweet(tweet_id)
    return render(request,'polls/tweet.html',{
      'username':user_screenname,
      'tweet':tweet
    })

def details(request):
    return HttpResponse("You're looking at our contact page.")