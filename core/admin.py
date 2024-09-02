from django.contrib import admin
from .models import Post, Category
from parler.admin import TranslatableAdmin


admin.site.register(Post, TranslatableAdmin)
admin.site.register(Category, TranslatableAdmin)
