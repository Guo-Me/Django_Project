from django.db import models


#048郭梦浩
class Product_Category(models.Model):
    category_name = models.CharField(max_length=20)
    category_img = models.CharField(max_length=200)
    category_ordernum = models.IntegerField()
    category_pid = models.IntegerField()
    create_time = models.DateTimeField()


#属性key
class ProductAttrKey(models.Model):
    #on_delete 级联删除
    category=models.ForeignKey('Product_Category',on_delete=models.CASCADE)
    attr_name = models.CharField(max_length=50)
    attr_order_num=models.IntegerField(default=1)
    #录取方式  1：手动录入 2：下拉选择
    enter_type = models.IntegerField(default=1)
    #是否是sku
    is_sku=models.IntegerField(default=0)
#属性value
class ProductAttrValue(models.Model):
    attr_key=models.ForeignKey('ProductAttrKey',on_delete=models.CASCADE)
    attr_value_name=models.CharField(max_length=50)
#商品表
class Product(models.Model):
    product_title=models.CharField(max_length=500)
    product_main_img=models.CharField(max_length=200)
    product_slide_img=models.CharField(max_length=1000)
    product_detail = models.CharField(max_length=3000)
    product_sku=models.CharField(max_length=1000)
    product_price=models.FloatField()
    product_stock=models.IntegerField()
    product_ordernum =models.IntegerField()
#郭梦浩

#SKU表
class ProductSku(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    product_price=models.FloatField()
    product_stock=models.IntegerField()
    product_sku=models.CharField(max_length=1000)
