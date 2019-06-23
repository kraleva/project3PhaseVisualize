from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('details/', views.details, name='details'),
    path('<str:user_screenname>/', views.users, name='user'),
    # ex: /polls/5/results/
    path('<str:user_screenname>/tweets/', views.tweets, name='tweets'),
    # ex: /polls/5/vote/
]


