from django.shortcuts import render,HttpResponse,redirect
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

        category_list=Product_Category.objects.all().filter(category_pid=0).values('id','category_ordernum','category_name','category_img',)
        datas = list(category_list)
        for categories in datas:
            categories["children"]=[]
            get_categories(categories)
            # print(categories)
        draw = request.POST.get("draw")

        #print(draw)
        result = {'draw':draw,'data':datas}
        json_str = json.dumps(result,ensure_ascii=False)


        return HttpResponse(json_str,content_type="application/json,charset=utf-8")

def get_categories(parent_category):
    #获取所有子节点的信息
    category = Product_Category.objects.filter(category_pid=parent_category["id"]).values('id','category_ordernum','category_name','category_img')
    sub_list = list(category)
    if len(sub_list) == 0:
        #如果没有子节点，直接返回，递归终止
        return
    #将子节点的信息给children属性
    parent_category['children']=sub_list
    for categories in sub_list:
        categories['children']=[]
        get_categories(categories)

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


def delete(request):

    if request.method == 'POST':
        id =request.POST.get('id')
        img = list(Product_Category.objects.filter(id=id).values('category_img'))[0]['category_img']
        path=  settings.MEDIA_ROOT +os.path.sep+'category_img'+ os.path.sep+img
        os.remove(path)
        Product_Category.objects.filter(id=id).delete()


    result = {'state': True}
    json_str = json.dumps(result, ensure_ascii=False)
    return HttpResponse(json_str, content_type="application/json,charset=utf-8")


def update(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        parent = Product_Category.objects.all().values('id','category_pid','category_name')
        categories=Product_Category.objects.get(id=id)
        return render(request,'product/category_update.html',{"category_list":categories,"parent":parent})
    elif request.method == 'POST':
        id = request.POST.get('id')
        fields ={}
        fields["category_ordernum"] = request.POST.get('category_ordernum')

        fields["category_pid"] = request.POST.get("category_pid")

        fields["category_name"] = request.POST.get("category_name")
        if dict(request.FILES):
            category_img = request.FILES["category_img"]
            category_img_name = category_img.name
            date_str = time.strftime("%Y%m%d%H%M%S", time.localtime())
            str_random = str(random.randint(10000, 99999))
            new_file_name = date_str + str_random + os.path.splitext(category_img_name)[1]
            img = new_file_name
            # os.path.sep 获取当前系统下的分隔符
            path = settings.MEDIA_ROOT + os.path.sep + "category_img" + os.path.sep
            # 上传文件
            with open(path + new_file_name, 'wb')as f:
                # 分块上传分件
                for chunk in category_img.chunks():
                    f.write(chunk)

            fields["category_img"]=img
        result=Product_Category.objects.filter(id=id).update(**fields)
        result = {'state': True if result>0 else False}
        # 禁用ascii编码
        json_str = json.dumps(result, ensure_ascii=False)
        return HttpResponse(json_str, content_type="application/json,charset=utf-8", )