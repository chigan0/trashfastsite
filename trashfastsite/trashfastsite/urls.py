"""trashfastsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static,serve
from trash_modul.views import *

urlpatterns = [
	path('',test),
	path('uebaka/', admin.site.urls),
	path('get_cate/',get_cate),
	path('cate/get/<str:resu>/',game_cate),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404='trash_modul.views.error_404_view'
handler500='trash_modul.views.error_500_view'
#handler403='trash_modul.views.error_404_view'
handler400='trash_modul.views.error_400_view'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^images/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),]
