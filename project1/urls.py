"""project1 URL Configuration

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
from apps.views import madhu
from apps.views import abijith
from apps.views import abi
from apps.views import fourth
from apps.views import fifth
urlpatterns = [
    path('admin/', admin.site.urls),
    path('madhu/',madhu , name='madhu'),
    path('abijith/',abijith,name='abijith'),
    path('abi/',abi,name='abi'),
    path('fourth/',fourth,name='fourth'),
    path('fifth/',fifth,name='fifth')
]
