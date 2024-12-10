from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class Admin(admin.ModelAdmin):
    list_display=['title']

