# encoding=utf8

"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views
from django.conf.urls import url
from snippets import views as snippetsviews

# from django.conf.urls.static import static
# from django.conf import settings




router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# 使用URL路由来管理我们的API
# 另外添加登录相关的URL
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^snippets/$', snippetsviews.snippet_list),
    url(r'^snippets/(?P<pk>.+)/$', snippetsviews.snippet_detail),
    # 挡板配置
    url(r'^mockconfig/$', snippetsviews.mockconfig_list),
    url(r'^mockhistory/$', snippetsviews.mockconfig_history),

    # 策略包字段
    url(r'^strategy/$', snippetsviews.strategy_list),
    url(r'^strategy/(?P<id>.+)/$', snippetsviews.strategy_detail),
    url(r'^strategyfield/$', snippetsviews.strategy_field_list),
    url(r'^strategyfield/(?P<id>.+)/$', snippetsviews.strategy_field),
    #获取当前实时出参
    url(r'^currentoutputsjson/$', snippetsviews.getCurrentOutputsJson),
    url(r'^currentoutputsjson/(?P<cid>.+)/$', snippetsviews.getCurrentOutputsJson),
    url(r'^reportlist/$', snippetsviews.report_list),
    url(r'^reportlist/(?P<id>.+)/$', snippetsviews.report_detail),
    url(r'^publishsqs/$', snippetsviews.publishSqs),
    url(r'^checkapply/$', snippetsviews.checkApply),
    url(r'^upload/$', snippetsviews.FileUploadView.as_view()),
    url(r'^download/$', snippetsviews.file_download),
    url(r'^jenkins/job/triger/$', snippetsviews.jenkins_job_triger),
    url(r'^jenkins/job/checkstatus/lastbuild/$', snippetsviews.jenkins_check_status_by_lastbuild),
    url(r'^jenkins/job/checkstatus/id/$', snippetsviews.jenkins_check_status_by_id),
    url(r'^updatedb/$', snippetsviews.updatedb),
    url(r'search/execution/$',snippetsviews.query_execution_names),
    url(r'personalInfo/(?P<cid>.+)/$',snippetsviews.get_person_info),
    url(r'changePersonInfo/$', snippetsviews.change_person_info),
]




