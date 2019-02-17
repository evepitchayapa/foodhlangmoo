import datetime
from  django.utils import timezone
from django.db import models


class Restaurants(models.Model):
    name_text = models.CharField(max_length=200)
    category = models.CharField(max_length = 100)
    route = models.CharField(max_length=250,default= '')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name_text



class Detail_res(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete = models.CASCADE)
    topic_review = models.CharField(max_length = 120,default= '')
    point = models.IntegerField(default = 0)
    review_text = models.CharField(max_length = 300)


    def __str__(self):
        return self.topic_review
