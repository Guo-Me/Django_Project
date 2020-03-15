from django.db import models


#048郭梦浩
class Product_Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_img = models.CharField(max_length=200)
    category_ordernum = models.IntegerField()
    category_pid = models.IntegerField()
    create_time = models.DateTimeField()
