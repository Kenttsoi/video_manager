from django.contrib import admin
from .models import Video, Actor, Publisher

@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'code_primany', 'release_month', 'publisher')
    search_fields = ('title', 'code_primany', 'description')
    list_filter = ('release_month', 'publisher')

admin.site.register(Publisher)

class VideoInline(admin.TabularInline):
    model = Video.actors.through
    extra = 0

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    list_display = ('name',)