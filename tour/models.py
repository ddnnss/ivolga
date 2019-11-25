from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string

class Country(models.Model):
    name = models.CharField('Страна', max_length=100, blank=False, null=True)

class Town(models.Model):
    name = models.CharField('Город', max_length=100, blank=False, null=True)

class Resort(models.Model):
    name = models.CharField('Курорт', max_length=100, blank=False, null=True)

class TourOption(models.Model):
    name = models.CharField('Опция', max_length=100, blank=False, null=True)

class Hotel(models.Model):
    name = models.CharField('Отель', max_length=100, blank=False, null=True)
    category = models.IntegerField('Категория (1-5), если указано 0, то категория не отображается', default=0)


class Tour(models.Model):
    name = models.CharField('Название тура', max_length=100, blank=False, null=True)
    name_lower = models.CharField(max_length=100, blank=False, null=True, db_index=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    short_description = models.TextField('Краткое описание для главной', blank=False)
    description = RichTextUploadingField('Полное описание тура', blank=False, null=True)

    includedOptions = models.ManyToManyField(TourOption, verbose_name='Входит в стоимость',
                                             related_name='includedOptions')
    excludedOptions = models.ManyToManyField(TourOption, verbose_name='Не входит в стоимость',
                                             related_name='excludedOptions')

    previewImage = models.ImageField('Изображение превью (360 x 240)', upload_to='tour_img/', blank=False)
    headerImage = models.ImageField('Изображение шапки страницы полного описания тура', upload_to='tour_img/', blank=False)

    pageH1 = models.CharField('Тег H1', max_length=255, blank=True, null=True)
    pageTitle = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    pageDescription = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    pageKeywords = models.TextField('Keywords SEO', blank=True, null=True)

    views = models.IntegerField('Просмотров', default=0)

    isAtIndex = models.BooleanField('Отображать на главной?', default=False)
    isActive = models.BooleanField('Отображать в списке туров?', default=True)
    priceDollar = models.IntegerField('Стоимость в долларах', default=0)
    discountPriceDollar = models.IntegerField('Стоимость со скидкой в долларах', default=0)

    priceEuro = models.IntegerField('Стоимость в евро', default=0)
    discountPriceEuro = models.IntegerField('Стоимость со скидкой в евро', default=0)

    priceRub = models.IntegerField('Стоимость в рублях', default=0)
    discountPriceRub = models.IntegerField('Стоимость со скидкой в рублях', default=0)

    length = models.IntegerField('Продолжительность тура', default=0)
    flyFrom = models.ForeignKey(Town, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Вылет из')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        testSlug = Tour.objects.filter(name_slug=slug)
        slugRandom = ''
        if self.name_slug != slug:
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.name_slug = slug + slugRandom
            else:
                self.name_slug = slug
        self.name_lower = self.name.lower()
        super(Tour, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/tour/{self.name_slug}/'

    def __str__(self):
        return 'Тур : %s ' % self.name

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
