"""SUAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),

    url(r'^about/$', views.about, name='about'),
    url(r'^converter/$', views.calculator, name='calculator'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gallery/upload/$', views.gallery_upload, name='gallery_upload'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^news/$', views.news, name='news'),
    url(r'^signin/$', views.user_logining, name='logining'),
    url(r'^signup/$', views.user_register, name='register'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
