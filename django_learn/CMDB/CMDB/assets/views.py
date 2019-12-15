from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from assets import models
from assets import asset_handler
# Create your views here.
@csrf_exempt
def report(request):
    if request.method == "POST":
        asset_data = request.POST.get('asset_data')
        data = json.loads(asset_data)
        if not data:
            return HttpResponse("没有数据！")
        if not issubclass(dict,type(data)):
            return HttpResponse("数据必须是字典格式！")
        sn = data.get('sn',None)
        if sn:
            #进入审批流程
            #首先判断是否在上线资产中存在该sn
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                #进入已上线资产的更新流程
                pass
                return HttpResponse("资产数据已经更新！")
            else:
                obj = asset_handler.NewAsset(request,data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)

        else:
            return HttpResponse("没有资产sn序列化，请检查数据")
    return HttpResponse("200 ok")