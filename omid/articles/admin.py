from django.contrib import admin
from articles.models import Article ,Comment ,Gallery

class ArticleAdmin(admin.ModelAdmin):
    list_display =['id','title','image','is_active']

class CommentAdmin(admin.ModelAdmin):
    list_display= ['id' , 'content' , 'related_article', 'related_user']

class GalleryAdmin(admin.ModelAdmin):
    list_display= ['id' , 'related_article', 'related_user', 'image']



admin.site.register(Article , ArticleAdmin)
admin.site.register(Comment, CommentAdmin) 
admin.site.register(Gallery, GalleryAdmin) 