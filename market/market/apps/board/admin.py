from django.contrib import admin

# Register your models here.
from market.apps.board.models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
