"""demo URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from demo_learn import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'create/$', views.create),
    # url(r'^getlist/$', views.get_list, name='get-list'),
    # path('admin/', admin.site.urls),
    # path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^movie/$', views.MovieList.as_view(), name='movie-list'),
    url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieDetail.as_view(),
        name='movie-detail'),
    path('admin/', admin.site.urls),
]
