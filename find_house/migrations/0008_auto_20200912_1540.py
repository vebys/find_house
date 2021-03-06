# Generated by Django 3.1 on 2020-09-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_house', '0007_auto_20200811_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='actual_area',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='实得面积'),
        ),
        migrations.AddField(
            model_name='house',
            name='house_lift',
            field=models.CharField(blank=True, default=0, max_length=20, null=True, verbose_name='梯户比'),
        ),
        migrations.AddField(
            model_name='house',
            name='single_price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='单价'),
        ),
        migrations.AlterField(
            model_name='house',
            name='area',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='面积'),
        ),
        migrations.AlterField(
            model_name='house',
            name='build',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='楼栋单元'),
        ),
        migrations.AlterField(
            model_name='house',
            name='flor',
            field=models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='楼层房号'),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='总价(万元)'),
        ),
        migrations.AlterField(
            model_name='house',
            name='year',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='建筑年代'),
        ),
    ]
