from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404
from .models import User,Tweet
from django.db.models import Q
from . forms import NameForm
from django import forms

def index(request):
  if request.method == 'GET':
    query = request.GET.get('screenname')
    form = NameForm(request.GET)
    if query:
      latest_user_list = User.objects.filter(screenname=str(query))
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
        user = User.objects.filter(screenname=str(user_screenname))
        user_attributes = user.values()
        if(len(user_attributes)):

        #print(user_attributes[0]['screenname'])
          tweets = Tweet.objects.filter(user=user_attributes[0]['user_id'])
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/user.html', {
      'tweets': tweets.values(),
      'user': user_attributes[0]})


def tweets(request,user_screenname):
    response = "You're looking at the tweets of user %s."
    return HttpResponse(response % user_screenname)

def details(request):
    return HttpResponse("You're looking at our contact page.")