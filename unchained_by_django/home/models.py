import datetime
from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=75)
    bio = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    def __str2__(self): return self.bio
	
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    desc = models.CharField(max_length=2000)
    def __str__(self): return self.title
    def __dte__(self): return self.date
    def __str2__(self): return self.author.name
    def __str3__(self): return self.desc
    def was_published_recently(self): return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


