from django.db import models

class Banner(models.Model):
    order = models.IntegerField('Номер по порядку', default=1)
    bannerOffer= models.CharField('Категория баннера (20символов)', max_length=20, blank=False)
    bigTextColored = models.CharField('Заголовок на баннере выделенный цветом (10символов)', max_length=10, blank=False, null=True)
    bigText = models.CharField('Заголовок на баннере (30 символов)', max_length=30, blank=False, null=True)
    smallText = models.CharField('Описание на баннере (160 символов)', max_length=160, blank=False, null=True)
    image = models.ImageField('Картинка для баннера (1920 x 900)', upload_to='banners/', blank=True)
    buttonText = models.CharField('Надпись на кнопке', max_length=10, blank=False)
    buttonUrl = models.CharField('Ссылка с кнопки', max_length=100, blank=False)
    isActive = models.BooleanField('Отображать баннер?', default=True)

    def __str__(self):
        return f'Баннер № П/П {self.order}'

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
