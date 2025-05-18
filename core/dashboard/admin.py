from django.contrib import admin
from . models import Folder,File

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display=['name','parent','owner']
    search_fields=['name']
    list_filter=['parent','owner']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display=['name','file','folder','size']
    search_fields=['name']
    list_filter=['folder','owner']

