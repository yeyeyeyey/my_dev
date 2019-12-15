from django.urls import path
from django.contrib import admin
from . import views
#命名空间
app_name = 'polls'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:question_id>/',views.detail,name = 'detail'),
    path('<int:question_id>/result',views.results,name = 'result'),
    path('<int:question_id>/vote',views.vote,name = 'vote'),

]

# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.error