from django.contrib import admin
from .models import Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('message','status','date_add','date_update')
    list_filter = ('user','status','date_add','date_update')
    search_field = ('message')
    list_per_page = 5
    date_hierarchy='date_add'