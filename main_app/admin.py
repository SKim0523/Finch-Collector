from django.contrib import admin
from .models import Finch, Comment, List
# Register your models here.
admin.site.register(Finch)
admin.site.register(Comment)
admin.site.register(List)
