from django.contrib import admin
from demo_learn import models
from rest_framework.pagination import LimitOffsetPagination
# from hys_operation.models import *
from django.utils.html import format_html
# Register your models here.

class MovieAdmin(admin.ModelAdmin):

    list_display = ('title','score','info','director','actor')
    search_fields = ('title',)
    list_filter = ('title',)
    # fields = (('title','score','info','director','actor'),)
    date_hierarchy = "create_time"
    fieldsets = (('文章内容',{'fields':['title','score','info'],'classes':(
        'wide','extrapretty'),}),
                 ('制作人员',{'fields':['director','actor'],'classes':(
                     'collapse',),}))
    # filter_horizontal = ('create_time',)
    list_per_page = 20
    list_display_links = ['title','score']
    # radio_fields = {'score': admin.VERTICAL}
    # list_editable = ['update_time']

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','age')


# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'colored_name')


# class MyAdminSite(admin.AdminSite):
#     site_header = "豆瓣排行200电影"            #设置页面显示表土
#     site_title = "豆瓣电影管理系统"

# admin.site = MyAdminSite(name='management')
admin.site.register(models.DoubandbMovies,MovieAdmin)
admin.site.register(models.Person,PersonAdmin)
# admin.sites.AdminSite.site_header = '豆瓣排行200电影'
# admin.sites.AdminSite.site_title = '豆瓣电影管理系统'

admin.site.site_header = '豆瓣电影管理系统'
admin.site.site_title = '豆瓣排行200电影'
admin.site.site_index = '豆瓣排行100电影'

class StandarResultSetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_description = 'limit'
    offset_query_param = 'offset'
    # offset_query_description = ''
    max_limit = None
