from django.db import models


class Articles(models.Model):
    start = models.TextField('Входные данные')
    finish = models.TextField('Обезличенные данные')
    

    def __str__(self):
        return self.start

    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'
