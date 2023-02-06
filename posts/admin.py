from django.contrib import admin

from posts.models import Post # new

admin.site.register(Post)     # new