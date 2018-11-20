from django.contrib import admin

# Register your models here.
from .views import Comment

admin.site.register(Comment)