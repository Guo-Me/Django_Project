# Generated by Django 2.2.5 on 2020-02-21 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Categroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categroy_name', models.CharField(max_length=20)),
                ('categroy_img', models.CharField(max_length=200)),
                ('categroy_ordernum', models.IntegerField()),
                ('categroy_pid', models.IntegerField()),
                ('create_time', models.DateTimeField()),
            ],
        ),
    ]
