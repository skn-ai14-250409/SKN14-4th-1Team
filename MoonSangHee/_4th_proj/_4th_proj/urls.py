"""
URL configuration for _4th_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')), # /app/으로 시작하는 요청을 app/urls.py로 위임
    path('', RedirectView.as_view(url='/app/')), # /루트 주소/로 접속하면 자동으로 /app/으로
    # path('uauth/', include('uauth.urls')), 
]

# 업로드파일 경로설정
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)