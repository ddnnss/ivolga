from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
#from pages.sitemaps import *

admin.site.site_header = "VOLGATOUR"
admin.site.site_title = "VOLGATOUR администрирование"
admin.site.index_title = "VOLGATOUR администрирование"

# sitemaps = {
#     'static': StaticViewSitemap,
#     'services': ServicesSitemap,
#     'blog': BlogSitemap
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    #path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    # path('item/', include('item.urls')),
    # path('cart/', include('cart.urls')),
    # path('user/', include('customuser.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)