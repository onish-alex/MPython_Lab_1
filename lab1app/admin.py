from django.contrib import admin
from .models import File, FileStatistics, FileStatisticsAdmin

admin.site.register(File)
admin.site.register(FileStatistics, FileStatisticsAdmin)