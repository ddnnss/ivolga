from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *
from blog.models import BlogPost
from tour.models import Tour

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['services','allposts','index','about']

    def location(self, item):
        return reverse(item)


class TourSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return Tour.objects.all()


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.created_at

