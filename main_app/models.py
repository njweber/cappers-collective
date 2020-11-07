from django.db import models

# Create your models here.
class tweet(models.Model):
    user = models.TextField(max_length= 50)
    date = models.DateField()
    text = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "tweet"