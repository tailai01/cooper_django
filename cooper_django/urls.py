"""cooper_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# 初始模块总路由
urlpatterns = [
    path('admin/', admin.site.urls),
    # 导入子应用的路由, users/ url上需要加上users/   eg:http://127.0.0.1:8000/users/username/iii/count
    # path('', include('apps.users.urls'))  这种URL上不需要加 eg: http://127.0.0.1:8000/username/iii/count
    path('users/', include('apps.users.urls')),
]
