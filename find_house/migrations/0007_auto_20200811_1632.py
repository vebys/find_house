# Generated by Django 3.1 on 2020-08-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_house', '0006_auto_20200811_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='period',
            field=models.CharField(default=None, max_length=40, verbose_name='学段'),
        ),
    ]