from django.urls import path

from . import views

urlpatterns = [
                path('', views.index),
                path('<unique_squirrel_id>/', views.details, name='update'),
                path('add/', views.add, name='add'),
                path('stats', views.stats, name='stats'),
                        ]
