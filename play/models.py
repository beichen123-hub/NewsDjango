from django.db import models

# Create your models here.

class NewsType(models.Model):
    tName = models.CharField(max_length=50, null=True, unique=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    class Meta():
        db_table = "NewsType"

class NewsInfo(models.Model):
    tid = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    nTitle = models.CharField(max_length=100, null=True)
    nAuthor = models.CharField(max_length=20, null=True)
    nContent = models.CharField(max_length=1000, null=True)
    nPubDateTime = models.DateTimeField(auto_now_add=True)
    Nstatus = models.BooleanField()
    class Meta():
        db_table = "NewsInfo"