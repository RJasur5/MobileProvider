from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.Logout, name='logout'),

    path('', views.home, name='home'),
    path('ProvidersCreate/', views.ProvidersCreate, name='ProvidersCreate'),

    path('dealers/', views.dealers, name='dealers'),
    path('dealersCreate/', views.dealersCreate, name='dealersCreate'),
    path('dealersUpdate/<str:pk>', views.dealersUpdate, name='dealersUpdate'),
    path('dealersDelete/<str:pk>', views.dealersDelete, name='dealersDelete'),

    path('NumberCode/', views.NumberCode, name='NumberCode'),
    path('NumberCodeCreate/', views.NumberCodeCreate, name='NumberCodeCreate'),
    path('NumberCodeUpdate/<str:pk>', views.NumberCodeUpdate, name='NumberCodeUpdate'),
    path('NumberCodeDelete/<str:pk>', views.NumberCodeDelete, name='NumberCodeDelete'),

    path('phone_numbers/<str:pk>', views.phonenumbers, name='phone_numbers'),
    path('PhoneNumbersCreate/<str:pk>', views.PhoneNumbersCreate, name='PhoneNumbersCreate'),
    path('PhoneNumbersUpdate/<str:pk>', views.PhoneNumbersUpdate, name='PhoneNumbersUpdate'),
    path('PhoneNumbersDelete/<str:pk>', views.PhoneNumbersDelete, name='PhoneNumbersDelete'),

    path('customer/', views.customer, name='customer'),
    path('CustomerCreate/', views.CustomerCreate, name='CustomerCreate'),
    path('CustomerUpdate/<str:pk>', views.CustomerUpdate, name='CustomerUpdate'),
    path('CustomerDelete/<str:pk>', views.CustomerDelete, name='CustomerDelete'),

    path('category/', views.category, name='category'),
    path('CategoryCreate/', views.CategoryCreate, name='CategoryCreate'),
    path('CategoryUpdate/<str:pk>', views.CategoryUpdate, name='CategoryUpdate'),
    path('CategoryDelete/<str:pk>', views.CategoryDelete, name='CategoryDelete'),

    path('tariff/<str:pk>', views.tariff, name='tariff'),
    path('TariffCreate/<str:pk>', views.TariffCreate, name='TariffCreate'),
    path('TariffUpdate/<str:pk>', views.TariffUpdate, name='TariffUpdate'),
    path('TariffDelete/<str:pk>', views.TariffDelete, name='TariffDelete'),

    path('UserPage', views.UserPage, name='UserPage'),

    path('BuyBeelineNumber', views.BeelinePage, name="BeelinePage"),
    path('BuyUzmobileNumber', views.UzmobilePage, name="UzmobilePage"),
    path('BuyUcellNumber', views.UcellPage, name="UcellPage"),
    path('BuyMobiuzNumber', views.MobiuzPage, name="MobiuzPage"),
    path('BuyHumansNumber', views.HumansPage, name="HumansPage"),

    path('BuyNumber/<str:pk>', views.BuyNumber, name="BuyNumber"),

]