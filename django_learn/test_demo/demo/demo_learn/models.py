from rest_framework.pagination import LimitOffsetPagination
from django.contrib import admin
from django.db import models
from django.utils.html import format_html

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(null= True,blank= True)

    def __unicode__(self):
        return self.name

class DoubandbMovies(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    score = models.CharField(max_length=10, blank=True, null=True)
    info = models.CharField(max_length=100, blank=True, null=True)
    movie_site = models.CharField(max_length=100, blank=True, null=True)
    pic_site = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(verbose_name= '导演',max_length=50, blank=True, null=True)
    actor = models.CharField( verbose_name= '演员',max_length=50, blank=True,null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    # color_code = models.CharField(max_length=6,blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'doubandb_movies'
    def color_status(self):
        if self.info >= 9.5:
            color_code = 'red'
        elif self.info >= 9:
            color_code = 'green'
        else:
            color_code = 'blue'
        return format_html(
            '<span style = "color: #{};">{} {}</span>',
            color_code,self.info
        )

class StandarResultSetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_description = 'limit'
    offset_query_param = 'offset'
    # offset_query_description = ''
    max_limit = None

# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     color_code = models.CharField(max_length=6)
#
#     def colored_name(self):
#         return format_html(
#             '<span style = "color: #{};">{} {}</span>',
#             self.color_code,
#             self.first_name,
#             self.last_name,
#         )

