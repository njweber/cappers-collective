from django.db import models

# Create your models here.
class tweets_all(models.Model):
    date = models.DateField()
    name = models.TextField(max_length= 50)
    text = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "tweets_all"