# Generated by Django 2.2.5 on 2020-04-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_productattrkey_productattrvalue_productsku'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattrkey',
            name='attr_order_num',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productattrkey',
            name='enter_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productattrkey',
            name='is_sku',
            field=models.IntegerField(default=0),
        ),
    ]
