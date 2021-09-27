import uuid

import pafy
import requests
from io import BytesIO

from django.core.files import File


def download_youtube(url):
    video = pafy.new(url)
    best = video.getbest(video)
    realurl = best.url_https
    return download_video(realurl)


def download_video(url):
    breakpoint()
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)


def get_video(video_obj):
    if video_obj.original_url.startswith("https://youtube"):
        file_obj = download_youtube(video_obj.original_url)
    else:
        file_obj = download_video(video_obj.original_url)

    if file_obj is None:
        video_obj.status = False
    else:
        filename = str(uuid.uuid4())
        video_obj.file.save(filename + '.mp4', File(file_obj))
        video_obj.status = True
        video_obj.save()
