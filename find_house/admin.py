from django.contrib import admin
from find_house.models import School, Community, CommunitySchool, House

admin.site.site_title = "新格林测试"
admin.site.site_header = "新格林测试"
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'period', 'remark', 'status')


admin.site.register(School, SchoolAdmin)


class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'price', 'remark')


admin.site.register(Community, CommunityAdmin)

class CommunitySchoolAdmin(admin.ModelAdmin):
    list_display = ('community', 'school')


admin.site.register(CommunitySchool, CommunitySchoolAdmin)


class HouseAdmin(admin.ModelAdmin):
    list_display = ('community', 'build','flor','area','actual_area','price','intention','house_lift','is_lift','is_park','is_two_year','year','unit_type','remark','time')


admin.site.register(House,HouseAdmin)


"""   community = models.ForeignKey(to='Community',to_field='name', related_name='house_to_Community',on_delete=models.CASCADE,default=None, null=True,
                                  blank=True, verbose_name='小区')
    build = models.CharField(max_length=40, default=None, null=True, blank=True, verbose_name='楼栋')
    flor = models.CharField(max_length=40, default=None, blank=True, verbose_name='楼层房号')
    area = models.FloatField(default='', null=True, blank=True, verbose_name='面积')
    price = models.FloatField(default='', null=True, blank=True, verbose_name='总价(万元)')
    is_lift = models.BooleanField(choices=((True,'有'),(False,'无')),default=True,verbose_name='是否有电梯')
    is_park = models.BooleanField(choices=((True,'有'),(False,'无')),default=True,verbose_name='是否有地下停车场')
    is_two_year = models.BooleanField(choices=((True,'是'),(False,'否')),default=True,verbose_name='是否满两年')
    year = models.IntegerField(default='', null=True, blank=True, verbose_name='建筑年代')
    advantage = models.CharField(max_length=300, default=None, null=True, blank=True, verbose_name='优点')
    shortcoming = models.CharField(max_length=300, default=None, null=True, blank=True, verbose_name='缺点')
    unit_type = models.ImageField(upload_to='static/media/', default=None, null=True, blank=True, verbose_name='户型图')
    remark = models.TextField(max_length=600, default=None, null=True, blank=True, verbose_name='备注')
    record = models.TextField(max_length=600, default=None, null=True, blank=True, verbose_name='看房记录')"""
