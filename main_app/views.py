from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import requests
import sys
import tweepy
import Private
import DB_Methods


# Create your views here.
def main(request):
   return render(request, "../templates/main.html", {})

def button_crawl_twitter(request):
   if not request.user.is_authenticated:
        return render(request, "../templates/admin/login.html", {})

   auth = tweepy.OAuthHandler(Private.TWITTER_API_KEY, Private.TWITTER_API_SECRET)
   auth.set_access_token(Private.TWITTER_KEY, Private.TWITTER_SECRET)
   api = tweepy.API(auth)

   public_tweet = api.user_timeline("thecheeze222")[1]
   text = public_tweet.text
   date = public_tweet.created_at
   name = public_tweet.user.screen_name  
   url = public_tweet.id 
   result = DB_Methods.save_tweet(date, name, text, url)
   print(result)
   return render(request, "../templates/admin/crawl.html", {})
   
def crawl_twitter_output(request):
   data = "Success"
   return render(request, "../templates/home.html", {'data':data})