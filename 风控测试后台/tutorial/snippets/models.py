# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid


from django.db import models

# Create your models here.


from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


# 策略包
class Strategy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    strategy = models.CharField(max_length=100, blank=True, default='')
    alias = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    isDelete = models.BooleanField(default=False)
    testEnv = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('strategy',)

    def __str__(self):
        return self.id  # acts as your post_id

# 策略包字段
class StrategyFiled(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    strategy = models.ForeignKey(Strategy, related_name='strategyfiled', on_delete=models.CASCADE)
    creditName = models.CharField(max_length=100, blank=True, default='')
    service = models.CharField(max_length=100, blank=True, default='')
    interface = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    logic = models.TextField(blank=True, default='')
    remarks = models.TextField(blank=True, default='')
    result = models.TextField(blank=True, default='')
    testSuccess = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    # 参数类型input、output
    paramType = models.CharField(max_length=100, blank=True, default='')
    testEnv = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('created',)


# 报告


class ReportHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=True, default='');
    createWay = models.CharField(max_length=100, blank=True, default='');
    cid = models.CharField(max_length=100, blank=True, default='');
    sqs = models.CharField(max_length=200, blank=True, default='');
    content = models.TextField(blank=True, default='')
    remarks = models.TextField(blank=True, default='')
    isDelete = models.BooleanField(default=False)
    testEnv = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created',)

# strategyName 策略包名称
# strategyAlias 策略包别名
# field OneToOneField 关联管理字段
# interface 字段名q
# currentValueType当前值类型
# currentValue当前值（字符串存储）

class ReportField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report = models.ForeignKey(ReportHistory, related_name='reportfileds', on_delete=models.CASCADE)
    strategyName = models.CharField(max_length=100, blank=True, default='')
    strategyAlias = models.CharField(max_length=100, blank=True, default='')
    # field = models.OneToOneField(StrategyFiled,related_name='filed', blank=True, null=True)
    field = models.ForeignKey(StrategyFiled,related_name='filed', null=True, blank=True,on_delete=models.CASCADE, default = None)
    # 参数类型input、output
    paramType = models.CharField(max_length=100, blank=True, default='')
    interface = models.CharField(max_length=100, blank=True, default='')
    currentValueType = models.CharField(max_length=100, blank=True, default='')
    currentValue = models.CharField(max_length=100, blank=True, default='')
    testResult = models.TextField(blank=True, default='')
    isTestFaild = models.BooleanField(default=False)
    isTestSuccess = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    testEnv = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)







# 挡板

class MockConfig(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(max_length=100, blank=True, default='')
    json = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    isDelete = models.BooleanField(default=False)
    testEnv = models.CharField(max_length=100, blank=True, default='')
    decisionName = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

# 挡板历史
class MockConfigHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    json = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    subItems = models.TextField(blank=True, default='')
    isDelete = models.BooleanField(default=False)
    testEnv = models.CharField(max_length=100, blank=True, default='')
    decisionName = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
