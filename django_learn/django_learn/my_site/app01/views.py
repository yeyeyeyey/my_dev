# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import datetime
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound
from django.views import View

# Create your views here.
def see(args,**kwargs):
    print("执行业务参数")
    return HttpResponse('dsdsd')

def article_archives(request,arg1,arg2):
    return HttpResponse("article 动态2 %s-%s "%(arg1,arg2))
def article_archives2(request,arg1,arg2,slug):
    return HttpResponse("article 动态2 %s-%s-%s "%(arg1,arg2,slug))
def article2003(request):
    return HttpResponse("2003")

def get_time(request):
    now=datetime.datetime.now()
    html="<html><body>Now is %s<body></html>"% now
    print(request.scheme)
    print(request.path)
    print(request.method)
    return HttpResponse(html)
def index(request):
    print(request.content_type)
    print(request.GET,request.POST)
    # print(request.POST.get('f_test'))
    # print(request.FILES)
    # print(request.META)
    # for k,v in request.META.items():
    #     print(k,v)
    print(request.build_absolute_uri())
    return render(request,'form.html')
def downloan_file(request):
    f=open('static_data/workmanage.xls','rb')
    res= HttpResponse(f.read(),content_type='application/vnd.ms-excel',)
    res['Content-Disposition']='attachment;filename="dowmload.xls"'
    return res

def test(request):
    print('--test--')
    return HttpResponseNotFound('haha')
    # return HttpResponseRedirect("/")

class TestView(View):

    time=datetime.datetime.now()
    def get(self,request):
        return HttpResponse("class view get request %s" %self.time)

    def post(self,request):
        return HttpResponse("class view post request%s" %self.time)

class TestView2(TestView):
    time =10