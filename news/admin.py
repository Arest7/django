from django.contrib import admin
from .models import Articles, UploadFile

class MyModelAdmin(admin.ModelAdmin):
    list_display=('file',)

admin.site.register(Articles)
admin.site.register(UploadFile, MyModelAdmin)
