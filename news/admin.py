from django.contrib import admin
from .models import Editor, Article, tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('tags',)
    
admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(tag)