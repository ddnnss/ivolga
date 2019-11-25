from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def index(request):
    #allBanners = Banner.objects.filter(isActive=True).order_by('order')

    homeActive = 'current-menu-item'
    return render(request, 'pages/index.html', locals())

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: locaclhost\nSitemap: localhost/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")
