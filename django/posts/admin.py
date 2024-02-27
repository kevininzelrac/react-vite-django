from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin ):
    fieldsets = [
        #(None,               {'fields': ['id']}),
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['content']}),
        #(None,               {'fields': ['created_at']}),
        #(None,               {'fields': ['updated_at']}),
    ]
    list_display = ('id','title', 'content', 'created_at', 'updated_at')

admin.site.register(Post, PostAdmin)