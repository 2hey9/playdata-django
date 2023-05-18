"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
<<<<<<< HEAD
from django.conf.urls.static import static
from django.conf import settings
from pybo.views import base_views
from cal import urls
from django.shortcuts import render
from chat import views as chat
=======
from pybo.views import base_views
>>>>>>> 7b6cbf1e72421c0627645b95c9d67b2b4bfb2465

urlpatterns = [
    path('', lambda request: render(request, 'index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
<<<<<<< HEAD
    path('board/', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('cal/', include('cal.urls')), #새로운 cal app에 대한 path
    path("chat/", include("chat.urls")), 
    # '/' 에 해당되는 path
=======
    path('', base_views.index, name='index'),  
>>>>>>> 7b6cbf1e72421c0627645b95c9d67b2b4bfb2465
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)