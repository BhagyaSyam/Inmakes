from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo')
    # path('calculate/', views.calculate,name='calculate')

    #     path('contact/',views.contact,name='contact')
]
