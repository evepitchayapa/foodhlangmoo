import datetime
from  django.utils import timezone
from django.db import models


class Restaurants(models.Model):
    name_text = models.CharField(max_length=200)
    category = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name_text



class Detail_res(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete = models.CASCADE)
    point = models.IntegerField(default = 0)
    review_text = models.CharField(max_length = 200)


    def __str__(self):
        return self.review_text
