from django.db import models

class Callback(models.Model):
    name = models.CharField('Имя',max_length=255, blank=True, default='Нет данных')
    phone = models.CharField('Телефон', max_length=255, blank=True, default='Нет данных')
    email = models.CharField('Почта', max_length=255, blank=True, default='Нет данных')
    service = models.CharField('Услуга', max_length=255, blank=True, default='Нет данных')
    message = models.TextField('Сообщение', blank=True, default='Нет данных')
    created_at = models.DateTimeField('Дата заполнения', auto_now_add=True)


    def __str__(self):
        return 'Форма заказа звонка. Заполнена {}'.format(self.created_at)



    class Meta:
        verbose_name = "Форма заказа звонка"
        verbose_name_plural = "Формы заказа звонка"
