"""
URL configuration for protfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from foodies import views
app_name='foodies'

urlpatterns = [
    path('about.html', views.about, name='about.html'),
    path('blog_single.html', views.blog_single, name='blog_single.html'),
    path('category.html', views.category, name='category.html'),
    path('contact.html', views.contact, name='contact.html'),
    path('homepage_2.html', views.homepage_2, name='homepage_2.html'),
    path('index.html', views.index, name='index.html'),
    path('search.html', views.search, name='search.html'),
    path('kart', views.kart, name='kart'),
    path('order', views.order, name='order'),
    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    

    ###for user registratio, sign-in sign-out
    path('info', views.info, name = 'info'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

]