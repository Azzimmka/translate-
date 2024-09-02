from django.contrib import admin
from .models import Post
from parler.admin import TranslatableAdmin


admin.site.register(Post, TranslatableAdmin)
