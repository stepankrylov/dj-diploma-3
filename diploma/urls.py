"""diploma URL Configuration

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
from django.urls import path
from django.conf.urls import url
from app.views import view_index, view_phone, view_smartphones, view_empty_section, view_cart, view_login, view_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view_index, name='index/'),
    path('smartphones', view_smartphones, name='smartphones'),
    path('smartphones/', view_smartphones, name='smartphones/'),
    path('empty_section/', view_empty_section, name='empty_section/'),
    path('cart/', view_cart, name='cart/'),
    path('login/', view_login, name='login/'),
    path('logout/', view_logout, name='logout/'),
    url(r'^smartphones/(?P<slug>[\w-]+)/$', view_phone, name='smartphones/slug/'),
]
