# Generated by Django 3.1 on 2020-09-12 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('find_house', '0009_house_intention'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='看房时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house',
            name='intention',
            field=models.NullBooleanField(choices=[(True, '有'), (None, '备选'), (False, '无')], default=None, verbose_name='是否有意向'),
        ),
    ]
