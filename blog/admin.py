from django.contrib import admin
from blog.models import BlogPost,BlogComment

# Register your models here.
admin.site.register((BlogComment,BlogPost))

# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     class Media:
#         js= ('tinyinject.js',)
