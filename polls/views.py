from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404
from .models import User
from django.db.models import Q

def index(request):
    latest_user_list = User.objects.all()
    context = {
      'latest_user_list':latest_user_list
    }
    return render(request,'polls/index.html',context)

def users(request, user_screenname):
    try:
        user = User.objects.filter(screenname=str(user_screenname))
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/user.html', {'user': user.values()})


def tweets(request,user_screenname):
    response = "You're looking at the tweets of user %s."
    return HttpResponse(response % user_screenname)

def details(request):
    return HttpResponse("You're looking at our contact page.")