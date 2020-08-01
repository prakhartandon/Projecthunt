from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
      title=models.CharField(max_length=50, default='title')
      timestamp=models.DateTimeField()
      body_text=models.TextField(max_length=200,default='Type Text')
      url=models.TextField()
      pic=models.ImageField(upload_to='images/',default='no image')
      icon=models.ImageField(upload_to='images/',default='no image')
      total_votes=models.IntegerField(default=1)
           #image=models.ImageField(Upload_to='images/')
      hunter= models.ForeignKey(User, on_delete=models.CASCADE)
      #summary=models.CharField(max_length=200)
      def summary(self):
          return (self.body_text[:100])

      def format_timestamp(self):
          return(self.timestamp.strftime("%d %B %Y"))

      def __str__(self):
          return(self.title)
