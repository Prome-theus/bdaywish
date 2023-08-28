from django.contrib import admin
from django.urls import path
from bday import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('main/',views.main,name='main')
]