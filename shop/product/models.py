from django.db import models


#048郭梦浩
class Product_Categroy(models.Model):
    categroy_name = models.CharField(max_length=20)
    categroy_img = models.CharField(max_length=200)
    categroy_ordernum = models.IntegerField()
    categroy_pid = models.IntegerField()
    create_time = models.DateTimeField()
