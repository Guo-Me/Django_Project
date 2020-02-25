from django.shortcuts import render,HttpResponse

from .models import *

#48郭梦浩
def test(request):
    # Categroy = Product_Categroy()
    # Categroy.categroy_name ='手机'
    # Categroy.categroy_ordernum ='3'
    # Categroy.create_time='2020-2-21 10:00:42'
    # Categroy.categroy_pid='0'
    # Categroy.save()


    #Product_Categroy.objects.filter(categroy_name='手机').update(categroy_ordernum=4)

    Product_Categroy.objects.filter(categroy_name='手机').delete()

    return HttpResponse('Hello world')