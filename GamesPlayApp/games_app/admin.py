from django.contrib import admin
from django.utils.html import format_html

from .models import Game, Profile


class GameModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "rating", "summary", "image_url", "image_tag"]
    list_filter = ["title", "summary"]
    search_fields = ['title']
    ordering = ['-category']



    def image_tag(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image_url))
        return None


class UserModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "profile_picture", "image_tag"]
    list_filter = ["first_name", "last_name"]
    search_fields = ['first_name']
    ordering = ['-first_name']

    def image_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.profile_picture))
        return None


admin.site.register(Game, GameModelAdmin)
admin.site.register(Profile, UserModelAdmin)