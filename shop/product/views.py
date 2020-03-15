from django.shortcuts import render,HttpResponse
from shop import settings
from .models import *
import time
import random
import datetime
import os
import json
#48郭梦浩
def category_list(request):
    if request.method =="GET":
        return render(request, 'product/category_list.html')
    elif request.method == "POST":

        category_list=Product_Category.objects.all().values('id','category_ordernum','category_name','category_img')
        datas = list(category_list)
        draw = request.POST.get("draw")
        result = {'draw':draw,'data':datas}
        json_str = json.dumps(result,ensure_ascii=False)

        return HttpResponse(json_str,content_type="application/json,charset=utf-8")


def category_add(request):
    if request.method =='GET':
        category_list = Product_Category.objects.all().values('id', 'category_name')
        return render(request,'product/category_add.html',{'category_list':category_list})
    elif request.method == 'POST':
        category=Product_Category()
        category.category_name=request.POST.get("category_name")

        category.category_ordernum=request.POST.get("category_ordernum")
        category.create_time=datetime.datetime.now()
        category.category_pid=request.POST.get("category_pid")
        category_img=request.FILES["category_img"]
        category_img_name=category_img.name
        date_str = time.strftime("%Y%m%d%H%M%S",time.localtime())
        str_random = str(random.randint(10000,99999))
        new_file_name = date_str+str_random+os.path.splitext(category_img_name)[1]
        category.category_img=new_file_name
        #os.path.sep 获取当前系统下的分隔符
        path = settings.MEDIA_ROOT+os.path.sep+"category_img"+os.path.sep
        #上传文件
        with open(path+new_file_name,'wb')as f:
            #分块上传分件
            for chunk in category_img.chunks():
                f.write(chunk)

        category.save()
        #返回json 格式数据
        result = {'state':True}
        #禁用ascii编码
        json_str=json.dumps(result,ensure_ascii=False)
        return HttpResponse(json_str,content_type="application/json,charset=utf-8",)
