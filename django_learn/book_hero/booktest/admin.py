from django.contrib import admin
from booktest.models import BookInfo
admin.site.register(BookInfo)
admin.site.register(QuestionAdmin,)

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    admin.site.register(QuestionAdmin,QuestionAdmin)
    list_display = ['pk','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fields = ['bpub_date','btitle']
    fieldsets = [
        ('basic',{'fields':['btitle']}),
        ('more',{'fields':['bpub_date']}),
    ]