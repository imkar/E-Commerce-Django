from django.contrib import admin

# Register your models here.
from .models import  Comment

class CommentAdmin(admin.ModelAdmin):
    list_disply = ['subject','comment','user','product','rate']
    readonly_fields = ('subject','comment','user','product','rate')
admin.site.register(Comment,CommentAdmin)
