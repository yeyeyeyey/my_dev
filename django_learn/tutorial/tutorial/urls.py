"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include



urlpatterns = [
    url(r'^$',views.api_root),
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^snippets/$',views.SnippetList.as_view(),name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'users/$',views.UserList.as_view(),name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),
        name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)