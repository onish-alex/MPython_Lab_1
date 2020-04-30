from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from lab1.settings import MEDIA_ROOT, os
from django.db import models
from .models import File, FileStatistics


def index(request):
    files_list = File.objects.all()
    return render(request, "index.html", {"files_list" : files_list})
 
def download(request, path):
    file_path = os.path.join(MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            file_name = File.objects.get(file_content = path)
            statistic, created = FileStatistics.objects.get_or_create(
                defaults={
                "file": file_name,
                "download_count": 0
                },
                file = file_name)
            statistic.download_count = statistic.download_count + 1
            statistic.save(update_fields=['download_count'])
            return response

