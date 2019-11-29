# encoding=utf-8

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,StrategyFiled,Strategy,MockConfig,ReportHistory,ReportField, MockConfigHistory
#
#
# class SnippetSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         如果数据合法就创建并返回一个snippet实例
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         如果数据合法就更新并返回一个存在的snippet实例
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')



class StrategyFiledSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyFiled
        fields = ('id','creditName','strategy','service','interface','description','logic','result','remarks','testSuccess','paramType','isDelete','testEnv')



class StrategySerializer(serializers.ModelSerializer):
    strategyfiled = StrategyFiledSerializer(many=True,read_only=True)

    class Meta:
        model = Strategy
        fields = ('id','strategy','alias','strategyfiled','description','isDelete','testEnv')

class MockConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockConfig
        fields = ('id','title','json','description','testEnv','decisionName')

class MockConfigHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MockConfigHistory
        fields = ('id','title','json','description','subItems','testEnv','decisionName')

class ReportFieldSerializer(serializers.ModelSerializer):
    creditName = serializers.CharField(source='field.creditName',read_only=True)
    service = serializers.CharField(source='field.service',read_only=True)
    description = serializers.CharField(source='field.description',read_only=True)
    logic = serializers.CharField(source='field.logic',read_only=True)
    remarks = serializers.CharField(source='field.remarks',read_only=True)
    class Meta:
        model = ReportField
        fields = ('id','report','strategyName','strategyAlias','field','creditName','description','service','logic','remarks','paramType','interface','currentValueType','currentValue','testResult','isTestFaild','isTestSuccess','isDelete')

class ReportWithoutFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportHistory
        fields = ('id','title','createWay','cid','sqs','content','remarks','isDelete','created','testEnv')

class ReportSerializer(serializers.ModelSerializer):
    reportfileds = ReportFieldSerializer(many=True,read_only=True)
    class Meta:
        model = ReportHistory
        fields = ('id','title','createWay','cid','sqs','content','remarks','reportfileds','isDelete','created','testEnv')
        depth = 3




