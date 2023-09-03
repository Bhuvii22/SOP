# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('reg', views.registration_view, name='reg'),
    path('next',views.nextpage,name='next'),
    path('last',views.submit,name='last'),
    path('success',views.success,name='success'),
    path('favicon.ico', views.favicon_view, name='favicon'),
]


