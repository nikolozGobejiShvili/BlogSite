from django.contrib import admin
from project.models import Post, Comment

admin.site.register([Post, Comment])
# Register your models here.
