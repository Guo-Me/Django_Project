# Generated by Django 2.2.5 on 2020-03-05 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Categroy',
            new_name='Product_Category',
        ),
        migrations.RenameField(
            model_name='product_category',
            old_name='category_img',
            new_name='category_img',
        ),
        migrations.RenameField(
            model_name='product_category',
            old_name='categroy_name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='product_category',
            old_name='categroy_ordernum',
            new_name='category_ordernum',
        ),
        migrations.RenameField(
            model_name='product_category',
            old_name='categroy_pid',
            new_name='category_pid',
        ),
    ]