# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
    """ 账户表"""
    username = models.CharField(max_length=64,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)
    signature = models.CharField("签名",max_length=255,null=True)


class Article(models.Model):
    """文章表"""
    title =models.CharField(max_length=255,unique=True)
    content = models.TextField()
    account = models.ForeignKey("Account",on_delete=models.CASCADE)
    """on_delete 关联删除处理方式 1.CASCADE 2. PROTECT 3.SET_NULL 4.SEYT_DEFAULT"""
    tags = models.ManyToManyField("Tag",null=True)
    pub_date = models.DateTimeField()

class Tag(models.Model):
    """标签表"""
    name = models.CharField(max_length=64,unique=True)
    date = models.DateTimeField(auto_now_add=True)
