from django.contrib import admin

from videos.models import Video
from videos.signals import get_video


@admin.action(description="Download video")
def download_videos(modeladmin, request, queryset):
    for video in queryset:
        get_video(video)


class VideoModelAdmin(admin.ModelAdmin):
    list_display = ("id", "original_url", "file", "status", "user")
    actions = (download_videos, )


admin.site.register(Video, VideoModelAdmin)
