# Generated by Django 3.1 on 2020-08-11 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=90, verbose_name='小区名称')),
                ('place', models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='位置')),
                ('price', models.FloatField(blank=True, default=0, null=True, verbose_name='均价')),
                ('remark', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '小区列表',
                'verbose_name_plural': '小区列表',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60, unique=True, verbose_name='学校名称')),
                ('period', models.CharField(default=None, max_length=40, unique=True, verbose_name='学段')),
                ('remark', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='备注')),
                ('status', models.BooleanField(default=True, null=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '学校列表',
                'verbose_name_plural': '学校列表',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='house_to_Community', to='find_house.community', verbose_name='小区')),
            ],
        ),
        migrations.CreateModel(
            name='CommunitySchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_Community', to='find_house.community', verbose_name='小区')),
                ('school', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_school', to='find_house.school', verbose_name='学校')),
            ],
            options={
                'verbose_name': '小区学校对应表',
                'verbose_name_plural': '小区学校对应表',
            },
        ),
    ]
