"""
URL configuration for Mayakovka_2_backend project.

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
from django.contrib import admin
from django.urls import path
from locations.views import LocationView, ImagesView, UserAddView, ActionView, StatisticView

urlpatterns = [
    path('admin_mayakovka/', admin.site.urls),
    path('locations/', LocationView.as_view()),
    path('images/', ImagesView.as_view()),
    path('user_add/', UserAddView.as_view()),
    path('action_add/', ActionView.as_view()),
    path('statistic/', StatisticView.as_view())
]
