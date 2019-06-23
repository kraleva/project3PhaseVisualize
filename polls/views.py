from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,Http404
from .models import User,Tweet,Following
from django.db.models import Q
from . forms import NameForm
from django import forms
from datetime import datetime
from . getuserdata import getTweets

def index(request):
  if request.method == 'GET':
    query = request.GET.get('screenname')
    form = NameForm(request.GET)
    if query:
      latest_user_list = User.objects.filter(screenname__startswith=str(query))
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
          user_id = user_attributes[0]['user_id']
          #followers = Following.objects.filter(user=user_id).values()
          followers = Following.objects.filter(user_id = user_id).values()
          fans = []
          for follower in followers:
            newuser = User.objects.filter(user_id = follower['follower_id']).values()
            print(newuser)
            fans.append(newuser[0])
          return render(request, 'polls/user.html', {
          'tweets': tweets,
          'user': user_attributes[0],
          'followers': fans,
          'age': age,
          'form': form})
    except User.DoesNotExist:
        raise Http404("Question does not exist")


def tweets(request,user_screenname):
    response = "You're looking at the tweets of user %s."
    return HttpResponse(response % user_screenname)

def details(request):
    return HttpResponse("You're looking at our contact page.")