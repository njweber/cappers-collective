from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import requests
import sys

import tweet_functions

# Create your views here.
def main(request):
   return render(request, "../templates/main.html", {})

def button_crawl_twitter(request):
   if not request.user.is_authenticated:
        return render(request, "../templates/admin/login.html", {})
   tweet_functions.start_crawl()
   return render(request, "../templates/admin/crawl.html", {})
   
def crawl_twitter_output(request):
   data = "Success"
   return render(request, "../templates/home.html", {'data':data})