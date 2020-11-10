from django.contrib import admin

# Register your models here.
from .models import tweets_all

@admin.register(tweets_all)
class tweet_admin(admin.ModelAdmin):
    list_display = ['id','date','name','text','url']

