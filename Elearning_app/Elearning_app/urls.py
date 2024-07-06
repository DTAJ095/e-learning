"""Elearning_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Elearning_app import settings
from django.conf.urls.static import static
from users.views import index, login_user, create_user, logout_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', create_user, name='register'),
    path('logout/', logout_user, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
