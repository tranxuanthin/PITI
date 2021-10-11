"""PTIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from Home import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',views.home),
    path('productsinfo/<int:id>/',views.productsinfo,name='productsinfo'),
    path('cart/',views.cart,name='cart'),
    path('login/',views.loginr,name='login'),
    path('rlogin/',views.rlogin,name='rlogin'),
    path('logout/',views.logout_view,name='logout'),
    path('sigup/',views.sigup,name='sigup'),
    path('rsigup/',views.rsigup,name='rsigup'),
    path('productsinfo/<int:id>/',views.home,name='productsinfo'),
    path('addcart/',views.addcart,name='addcart'),
    path('category/<int:id>/',views.category,name='category'),
   
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
