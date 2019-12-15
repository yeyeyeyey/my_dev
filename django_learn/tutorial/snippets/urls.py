from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetViewSet,UserViewSet,api_root
snippet_list = SnippetViewSet.as_view({
    'get':'list',
    'post':'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get':'highlight'
},renderers_classes = [renderers.StaticHTMLRenderer])

user_detail = UserViewSet.as_view({
    'get':'retrieve'
})

user_list = UserViewSet.as_view({
    'get':'list'
})





urlpatterns = format_suffix_patterns([
    url(r'^$',api_root),
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^snippets/$',snippet_list,name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',snippet_detail,name='snippet-detail'),
    url(r'users/$',user_list,name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$',user_detail,
        name='user-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',snippet_highlight,
        name='snippet-highlight'),

])