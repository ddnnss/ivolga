from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string

class BlogPost(models.Model):
    name = models.CharField('Название (40 символов)', max_length=40, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение превью (555 x 390)', upload_to='blog_img/', blank=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=False, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=False, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=False, null=True)
    short_description = models.CharField('Краткое описание (100 символов)', max_length=100, blank=False)
    description = RichTextUploadingField('Статья', blank=False, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_at_index = models.BooleanField('Отображать статью на главной?', default=True, db_index=True)
    is_active = models.BooleanField('Отображать статью в списке всех статей?', default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        testSlug = BlogPost.objects.filter(name_slug=slug)
        slugRandom = ''
        if self.name_slug != slug:
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
                self.name_slug = slug + slugRandom
            else:
                self.name_slug = slug

        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/post/{self.name_slug}/'

    def __str__(self):
        return 'Статья : %s ' % self.name

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"

