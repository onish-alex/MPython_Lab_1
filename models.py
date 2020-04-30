from django.db import models
from django import forms 
from .validators import validate_file_extension
from django.contrib import admin

class File(models.Model):
    file_name = models.CharField('Имя файла', max_length=261)
    file_content = models.FileField('Файл', upload_to='documents/', validators=[validate_file_extension])

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.file_name)
        
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

class FileStatistics(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    download_count = models.IntegerField('Количество загрузок')
    
    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.file.file_name)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'
        ordering = ('-download_count',)

class FileStatisticsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'download_count')
    search_fields = ('__str__', )

    def has_change_permission(self, request, obj=None):
        return not bool(obj)

    def has_add_permission(self, request):
        return False
