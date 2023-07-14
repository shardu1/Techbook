from django.db import models

# Create your models here.

class News(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    imgurl = models.CharField(max_length=300)
    newsurl = models.CharField(max_length=300)
    description = models.TextField()
    query=models.CharField(max_length=20)
    date=models.DateField(blank=True)
    slug = models.CharField(max_length=230)

    def __str__(self): 
        return self.title
