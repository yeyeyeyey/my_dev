# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import json
import subprocess


from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse,HttpResponseRedirect


from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet,Strategy,StrategyFiled,MockConfig,MockConfigHistory, ReportHistory

from snippets.serializers import SnippetSerializer,StrategySerializer,StrategyFiledSerializer,MockConfigSerializer, MockConfigHistorySerializer, ReportSerializer,ReportWithoutFieldSerializer,ReportFieldSerializer

from snippets.utils import *
import json
import uuid
# import commands

from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.conf import settings
import boto3
import botocore
from django.utils.decorators import method_decorator


class JSONResponse(HttpResponse):
    """
    用于返回JSON数据.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



# 上传文件
@method_decorator(csrf_exempt,name='dispatch')
class FileUploadView(APIView):
    # parser_classes = (FileUploadParser, )
    parser_classes = (MultiPartParser,)
    def post(self, request, format=None):
        up_file = request.FILES.get('file',None)
        bucket_name = request.data.get('bucket_name')
        # print bucket_name
        key = request.data.get('key')
        file_name = key.split('/', -1)[-1]
        self.dispatch
        # print key

        # print up_file.chunks
        # print settings.STATICFILES_DIRS +'/' + up_file.name
        destination = open( settings.STATICFILES_DIRS[0]+'/upload/' + file_name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
        destination.close()
        # ...
        # do some stuff with uploaded file
        # ...
        # print settings.STATIC_URL
        s3 = boto3.client('s3')

        # bucket_name = 'mm-kr-test'
        # key = 'test1/credit/partner/QIDAI/2019/01/07/201901070000000131231546846487225'

        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        s3.upload_file(settings.STATICFILES_DIRS[0]+'/upload/' + file_name, bucket_name, key)
        return Response(settings.STATIC_URL+'upload/'+file_name)


# 文件下载
@csrf_exempt
def file_download(request):
    if request.method == 'GET':
        bucket_name = request.GET.get('bucket_name')
        # print bucket_name
        key = request.GET.get('key')
    # replace with your object key

    s3 = boto3.resource('s3')
    file_name = key.split('/',-1)[-1]

    try:
        s3.Bucket(bucket_name).download_file(key, settings.STATICFILES_DIRS[0]+'/download/'+file_name)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    # with open(settings.STATICFILES_DIRS[0]+'/201901070000000131231546846487224.txt') as f:
    #     c = f.read()
    # return HttpResponse(c)
    return HttpResponseRedirect(settings.STATIC_URL+'download/'+file_name)



# 发SQS

@csrf_exempt
def publishSqs(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        sqs = data.get('sqs')
        cid = data.get('cid')
        try:
            publishSQS(sqs,cid)
            return HttpResponse(status=200)
        except(Exception):
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=500)

# 查询审批进度
@csrf_exempt
def checkApply(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        cid = data.get('cid')
        # print cid
        try:
            return HttpResponse(checkApply(cid))
        except Exception:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=500)


# 查询报告列表

@csrf_exempt
def gitPushMock(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        mockText = data.get('mockText')
        try:
            gitPushMock(mockText)
            return HttpResponse(status=200)
        except Exception:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=500)



@csrf_exempt
def report_list(request):
    """
    展示所以snippets,或创建新的snippet
    """
    # import sys

    # reload(sys)
    # sys.setdefaultencoding('utf8')
    if request.method == 'GET':
        reports = ReportHistory.objects.filter(isDelete=False)
        serializer = ReportWithoutFieldSerializer(reports, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        strategyAliasMap = {
            "M_QD_FA1": "查询反欺诈1",
            "M_QD_FB1": "查询反欺诈2",
            "M_QD_FL1": "查询终审包",
            "M_QD_SE1": "查询评分卡",
            "M_QD_CT1": "查询额度包"
        }
        data = JSONParser().parse(request)
        # print 'data:'
        # print data
        cid = data.get('cid')
        report = None
        try:
            if (data.has_key('id')):
                id = data.get('id')
                report = ReportHistory.objects.get(id=id)
                reportSerializer = ReportWithoutFieldSerializer(report, data=data)
                if reportSerializer.is_valid():
                    report = reportSerializer.save()
                    if(data.has_key('id')):
                        return JSONResponse(reportSerializer.data)


            (allinputField, alloutputField, allStrategy) = createReport(cid);
            data['content'] = json.dumps(allStrategy,ensure_ascii=False)
            reportSerializer = ReportWithoutFieldSerializer(report, data=data)

            if reportSerializer.is_valid():
                report = reportSerializer.save()
                if(data.has_key('id')):
                    return JSONResponse(reportSerializer.data)

            for key in alloutputField:
                # print key
                strategyAlias = key
                strategyFilter = Strategy.objects.filter(alias=strategyAlias)
                if strategyFilter.count() == 1:
                    # print "策略包存在。"
                    strategy = Strategy.objects.get(alias=strategyAlias)

                for key,value in alloutputField[strategyAlias].items():
                    tmp = {}
                    tmp['paramType'] = 'output'
                    tmp['report'] = report.id
                    tmp['strategyAlias'] = strategyAlias
                    tmp['interface'] = key
                    tmp['currentValueType'] = type(value).__name__
                    # print "strategy.id:"
                    # print strategy.id
                    if strategy:
                        fieldFilter = StrategyFiled.objects.filter(strategy=strategy.id, interface=key)
                    # print "fieldFilter:"
                    # print fieldFilter
                    if fieldFilter.count() == 1:
                        tmp['field'] = StrategyFiled.objects.get(strategy=strategy.id,interface=key).id
                        # print "字段存在。"
                    # print type(value)
                    # tmp['field'] = 'b646d718-65f6-4054-9daa-aa220b9c1fd5'
                    if type(value) == (type(u"")):
                        tmp['currentValue'] = value
                        tmp['currentValueType'] = 'str'
                    else:
                        tmp['currentValue'] = str(value)
                    # print tmp
                    fieldSerializer = ReportFieldSerializer(data=tmp)
                    if fieldSerializer.is_valid():
                        pass
                        fieldSerializer.save()
                    else:
                        pass
                        # print fieldSerializer.error_messages
                        # print  fieldSerializer.errors
                for key in allinputField:
                    # print key
                    strategyAlias = key
                    strategyFilter = Strategy.objects.filter(alias=strategyAlias)
                    if strategyFilter.count() == 1:
                        # print "策略包存在。"
                        strategy = Strategy.objects.get(alias=strategyAlias)

                    for key, value in allinputField[strategyAlias].items():
                        tmp = {}
                        tmp['paramType'] = 'input'
                        tmp['report'] = report.id
                        tmp['strategyAlias'] = strategyAlias
                        tmp['interface'] = key
                        tmp['currentValueType'] = type(value).__name__
                        # print "strategy.id:"
                        # print strategy.id
                        if strategy:
                            fieldFilter = StrategyFiled.objects.filter(strategy=strategy.id, interface=key)
                        # print "fieldFilter:"
                        # print fieldFilter
                        if fieldFilter.count() == 1:
                            tmp['field'] = StrategyFiled.objects.get(strategy=strategy.id, interface=key).id
                            # print "字段存在。"
                        # print type(value)
                        # tmp['field'] = 'b646d718-65f6-4054-9daa-aa220b9c1fd5'
                        if type(value) == (type(u"")):
                            tmp['currentValue'] = value
                            tmp['currentValueType'] = 'str'
                        else:
                            tmp['currentValue'] = str(value)
                        # print tmp
                        fieldSerializer = ReportFieldSerializer(data=tmp)
                        if fieldSerializer.is_valid():
                            pass
                            fieldSerializer.save()
                        else:
                            pass
                            # print fieldSerializer.error_messages
                            # print  fieldSerializer.errors
            serializer = ReportWithoutFieldSerializer(report)
            return JSONResponse(serializer.data)
        except ReportHistory.DoesNotExist:
            return HttpResponse(status=404)




# 创建报告
@csrf_exempt
def report_detail(request,id):
    """
    展示所以snippets,或创建新的snippet
    """
    if request.method == 'GET':
        # print id
        report = ReportHistory.objects.get(id=id)
        # print report
        reportSerializer = ReportSerializer(report)
        # print JSONResponse(reportSerializer.data)
        return JSONResponse(reportSerializer.data)


# 获取单审批节点实际出参
@csrf_exempt
def getCurrentOutputsJson(request):
    testEnv = request.META.get('HTTP_TESTENV', 'unkown')
    if request.method == 'POST':
        data = JSONParser().parse(request)
        execute_action = data.get('execute_action')
        cid = data.get('cid')
        jsonStr = getCurrentJson(execute_action=execute_action,cid=cid,testEnv=testEnv)
        if jsonStr == "":
            return HttpResponse(status=404)
        else:
            return JSONResponse(jsonStr)



# 挡板配置接口
@csrf_exempt
def mockconfig_list(request):
    testEnv = request.META.get('HTTP_TESTENV', 'unkown')
    decisionName = request.META.get('HTTP_'+'decisionName'.upper(), 'unkown')
    configBranch = request.META.get('HTTP_'+'configBranch'.upper(), 'unkown')

    if request.method == 'POST':
        # pass
        data = JSONParser().parse(request)
        # data['testEnv'] = decisionName
        data['decisionName'] = decisionName
        mockconfig = None
        if (data.has_key('id')):
            id = data.get('id')
            mockconfig = MockConfig.objects.get(id=id)
        serializer = MockConfigSerializer(mockconfig,data=data)
        if serializer.is_valid():
            serializer.save()
        # return JSONResponse(serializer.data)

    elif request.method == 'DELETE':

        data = JSONParser().parse(request)
        id = data.get('id')
        # print id
        mockconfig = MockConfig.objects.get(id=id)
        mockconfig.delete()
        # return HttpResponse(status=204)
    mockconfig = MockConfig.objects.filter(decisionName=decisionName)
    # mockconfig = MockConfig.objects.all()
    serializer = MockConfigSerializer(mockconfig, many=True)
    return JSONResponse(serializer.data)

# 挡板历史
@csrf_exempt
def mockconfig_history(request):
    testEnv = request.META.get('HTTP_TESTENV', 'unkown')
    decisionName = request.META.get('HTTP_' + 'decisionName'.upper(), 'unkown')
    configBranch = request.META.get('HTTP_' + 'configBranch'.upper(), 'unkown')
    if request.method == 'POST':
        # pass
        data = JSONParser().parse(request)
        # print data['title']
        mockconfigHistory = None
        data['decisionName'] = decisionName
        if (data.has_key('id')):
            id = data.get('id')
            if id != "":
                mockconfigHistory = MockConfigHistory.objects.get(id=id)

        serializer = MockConfigHistorySerializer(mockconfigHistory,data=data)
        if serializer.is_valid():
            serializer.save()
        # return JSONResponse(serializer.data)

    elif request.method == 'DELETE':

        data = JSONParser().parse(request)
        # print data
        for id in data:
            if len(MockConfigHistory.objects.filter(id=id)) > 0:
                mockconfigHistory = MockConfigHistory.objects.get(id=id)
                mockconfigHistory.delete()
        # return HttpResponse(status=204)
    mockconfigHistory = MockConfigHistory.objects.filter(decisionName=decisionName)
    serializer = MockConfigHistorySerializer(mockconfigHistory, many=True)
    return JSONResponse(serializer.data)

# 策略包字段配置接口

@csrf_exempt
def strategy_list(request):
    """
    展示所以snippets,或创建新的snippet
    """
    if request.method == 'GET':
        strategy = Strategy.objects.filter(isDelete=False)
        serializer = StrategySerializer(strategy, many=True)
        return JSONResponse(serializer.data)


    elif request.method == 'POST':


        data = JSONParser().parse(request)
        # print 'data:'
        # print data
        strategy = None
        try:
            if( data.has_key('id')):
                id = data.get('id')
                strategy = Strategy.objects.get(id=id)
            if (data.has_key("strategyfiled")):
                for fieldData in data.get("strategyfiled"):
                    field = None
                    fieldData['strategy'] = id
                    if fieldData.has_key('id'):
                        field = StrategyFiled.objects.get(id=fieldData.get('id'))
                    fieldSerializer = StrategyFiledSerializer(field, data=fieldData)
                    if fieldSerializer.is_valid():
                        fieldSerializer.save()
            strategSerializer = StrategySerializer(strategy, data=data)
            if strategSerializer.is_valid():
                strategSerializer.save()
        except Strategy.DoesNotExist:
            return HttpResponse(status=404)

        strategy = Strategy.objects.filter(isDelete=False)
        serializer = StrategySerializer(strategy, many=True)
        return JSONResponse(serializer.data)

        #     return JSONResponse(strategSerializer.data, status=201)
        # return JSONResponse(strategSerializer.errors, status=400)


@csrf_exempt
def strategy_detail(request,id):
    """
    修改或删除一个snippet.
    """
    try:
        strategy = Strategy.objects.filter(isDelete=False).get(id=id)
    except Strategy.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StrategySerializer(strategy)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StrategySerializer(strategy, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        strategy.delete()
        return HttpResponse(status=204)


@csrf_exempt
def strategy_field_list(request):
    """
    展示所以snippets,或创建新的snippet.
    """
    if request.method == 'GET':
        field = StrategyFiled.objects.all()
        serializer = StrategyFiledSerializer(field, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        field = StrategyFiled.objects.get(id=data.get('id'))

        serializer = StrategyFiledSerializer(field,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        field = StrategyFiled.objects.get(id=data.get('id'))
        field.delete()
        return HttpResponse(status=204)

@csrf_exempt
def strategy_field(request, id):
    """
    展示所以snippets,或创建新的snippet.
    """
    if request.method == 'GET':
        # print "id:"+id
        field = StrategyFiled.objects.filter(id=id)
        # print field
        serializer = StrategyFiledSerializer(field, many=True)
        return JSONResponse(serializer.data[0])

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StrategyFiledSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_list(request):
    """
    展示所以snippets,或创建新的snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=204)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    修改或删除一个snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def jenkins_job_triger(request):
    """
    创建jenkins job
    :param request:
    :param jobName:
    :param data:
    :return:
    """
    # reload(sys)  # reload 才能调用 setdefaultencoding 方法
    # sys.setdefaultencoding('utf-8')  # 设置 'utf-8'
    testEnv = request.META.get('HTTP_TESTENV', 'unkown')
    decisionName = request.META.get('HTTP_'+'decisionName'.upper(), 'unkown')
    configBranch = request.META.get('HTTP_'+'configBranch'.upper(), 'unkown')

    if request.method == 'POST':
        data = JSONParser().parse(request)
        jobName = data.get('jobName')
        params = data.get('params')

        output = cmd('curl -s -I -XPOST  "http://10.3.208.42:8080/jenkins/job/'+ jobName +'/buildWithParameters?'+params+'" --user fengyu:Fengyu@1q')
        # print output
        return HttpResponse(content=output[1].split('\n')[2].split('/')[-2])
    else:
        return HttpResponse(content='error request method')

@csrf_exempt
def jenkins_check_status_by_lastbuild(request):
    """
    检查jenkins job 最后一次构建状态
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        jobName = data.get('jobName')
        output = cmd('curl -s http://192.168.157.131:8080/jenkins/job/'+jobName+'/lastBuild/api/json?tree=id,result,building,queueId,description')
        return JSONResponse(output[1])
    else:
        return HttpResponse(content='error request method')

class Replace(object):
    def repalce(self):
        pass




@csrf_exempt
def jenkins_check_status_by_id(request):
    """
    检查jenkins job 指定id构建状态
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        jobName = data.get('jobName')
        id = data.get('id')
        output = cmd('curl -s http://192.168.157.131:8080/jenkins/job/' + jobName + '/' + id + '/api/json?tree=id,result,building,queueId,description')
        return JSONResponse(output[1])
    else:
        return HttpResponse(content='error request method')

@csrf_exempt
def updatedb(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
     #  sqs = data.get('sqs')

        identity_no = data.get('identity_no')
        try:
            customer_update(identity_no)
            return HttpResponse(status=200)
        except Exception as e:
            # print e
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=500)

@csrf_exempt
def query_execution_names(request):
    testEnv = request.META.get('HTTP_TESTENV', 'unkown')
    decisionName = request.META.get('HTTP_'+'decisionName'.upper(), 'unkown')
    if request.method == 'POST':
        data = JSONParser().parse(request)
        key = data.get('key')
        # print request.META
        return HttpResponse(content=query_execute_action_name(testEnv,decisionName,key))
    else:
        return HttpResponse(status=500)


# @csrf_exempt
def get_person_info(request,cid):
    if request.method =='GET':
        testEnv = request.META.get('HTTP_TESTENV')
        data = get_credential_point(testEnv,cid)[1]
        # print(data)
        # print("~~~~~!!!!!!!!~~~~~`")
        # return Response(content='error request method')
        # print(type(data))
        data2 = get_idcard_point(testEnv,cid)[1]
    # print(type(HttpResponse(data)))
    # print(type(JSONResponse(data)))
        list = [data,data2]
    return JSONResponse(data)
@csrf_exempt
def change_person_info(request):
    if request.method =='POST':
        data = JSONParser().parse(request)
        # print(type(data))
        # print(type(person_info))
        # print(person_info)
        testEnv = request.META.get('HTTP_TESTENV')
        # print(testEnv)
        # print("~~~~~~~~",type(testEnv))
        cid = data.get('cid')
        old_data = get_credential_point(testEnv,cid)[1]
        def replace(key):
            if data.get(key) is None:
                return old_data.get(key)
            else:
                return data.get(key)
        appchannel = replace('appchannel')
        census_address = replace('census_address')
        gpsAddress = replace('gpsAddress')
        idenNum = replace('idenNum')
        name = replace('name')
        device_info = replace('device_info')
        user_basic_data = {
            'name':name,'idenNum':idenNum
        }
        # dic = get_new_info(testEnv, cid, appchannel,
        #              census_address, gpsAddress,
        #              idenNum, name,device_info).encode('utf-8').decode("unicode_escape")
        dic = get_new_info(testEnv,cid,appchannel,census_address,gpsAddress,idenNum,
            name,device_info)
        update_info(testEnv, cid, dic)
        update_idcard_info(testEnv, cid, dic)
        update_cif_info(testEnv,cid,user_basic_data)
        # print(type(person_info))
        # new_person_info = json.dumps(person_info)
        return JSONResponse(data=get_credential_point(testEnv,cid)[1],
                            status=200)


