from django.db import models


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=60, default=None, verbose_name='学校名称', unique=True)
    period = models.CharField(max_length=40, default=None, verbose_name='学段')
    status = models.BooleanField(default=True,null=True,verbose_name='状态')
    area = models.ImageField(upload_to='static/media/', default=None, null=True, blank=True, verbose_name='片区图片')
    remark = models.TextField(max_length=600, default=None, null=True, blank=True, verbose_name='备注')

    class Meta:
        verbose_name = "学校列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + self.period


class Community(models.Model):
    name = models.CharField(max_length=90, default=None, verbose_name='小区名称',unique=True)
    place = models.CharField(max_length=120, default=None, null=True, blank=True, verbose_name='位置')
    price = models.FloatField(default='', null=True, blank=True, verbose_name='均价(万元)')
    remark = models.TextField(max_length=600, default=None, null=True, blank=True, verbose_name='备注')

    class Meta:
        verbose_name = "小区列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CommunitySchool(models.Model):
    community = models.ForeignKey(to='Community',to_field='name', related_name='to_Community',on_delete=models.CASCADE, default=None, null=True,
                                  blank=True, verbose_name='小区')
    school = models.ForeignKey(to='School', related_name='to_school',to_field='name', on_delete=models.CASCADE,default=None, null=True, blank=True,
                               verbose_name='学校')

    class Meta:
        verbose_name = "小区学校对应表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.community.name + self.school.name


class House(models.Model):
    """小区	楼栋	楼层房号	面积	总价	是否电梯	是否有地下停车场	年代	是否满两年	优点	缺点	房屋链接	看房记录	备注"""
    community = models.ForeignKey(to='Community',to_field='name', related_name='house_to_Community',on_delete=models.CASCADE,default=None, null=True,
                                  blank=True, verbose_name='小区')
    build = models.CharField(max_length=40, default=None, null=True, blank=True, verbose_name='楼栋单元')
    flor = models.CharField(max_length=40, default=None, null=True,blank=True, verbose_name='楼层房号')
    area = models.FloatField(default=0, null=True, blank=True, verbose_name='面积')
    actual_area = models.FloatField(default=0, null=True, blank=True, verbose_name='实得面积')
    price = models.FloatField(default=0, null=True, blank=True, verbose_name='总价(万元)')
    single_price = models.FloatField(default=0, null=True, blank=True, verbose_name='单价')
    intention = models.NullBooleanField(choices=((True, '有'), (None, '备选'), (False, '无')), default=None, verbose_name='是否有意向')
    house_lift = models.CharField(max_length=20, default=0, null=True, blank=True, verbose_name='梯户比')
    is_lift = models.BooleanField(choices=((True,'有'),(False,'无')),default=True,verbose_name='是否有电梯')
    is_park = models.BooleanField(choices=((True,'有'),(False,'无')),default=True,verbose_name='是否有地下停车场')
    is_two_year = models.BooleanField(choices=((True,'是'),(False,'否')),default=True,verbose_name='是否满两年')
    year = models.IntegerField(default=0, null=True, blank=True, verbose_name='建筑年代')
    advantage = models.CharField(max_length=300, default=None, null=True, blank=True, verbose_name='优点')
    shortcoming = models.CharField(max_length=300, default=None, null=True, blank=True, verbose_name='缺点')
    unit_type = models.ImageField(upload_to='static/media/', default=None, null=True, blank=True, verbose_name='户型图')
    remark = models.TextField(max_length=600, default=None, null=True, blank=True, verbose_name='备注')
    record = models.TextField(max_length=600, default=None, null=True, blank=True, verbose_name='看房记录')
    time = models.DateTimeField(auto_now_add=True, verbose_name='看房时间')


    class Meta:
        verbose_name = "房屋列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.community.name + self.build + self.flor