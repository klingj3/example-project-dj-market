from django.contrib import admin

from market.apps.board.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'body')


admin.site.register(Post, PostAdmin)
