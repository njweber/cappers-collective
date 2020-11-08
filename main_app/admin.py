from django.contrib import admin

# Register your models here.
from .models import tweet

@admin.register(tweet)
class tweet_admin(admin.ModelAdmin):
    list_display = ['id','user','date','text','url']

