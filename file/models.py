from django.db import models


class File(models.Model):
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    file = models.FileField(upload_to="files/", verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата загрузки файла')
    processed = models.BooleanField(default=False, verbose_name='Обработан')
