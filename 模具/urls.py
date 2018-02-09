from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('Muju/<int:muju_id>/', views.detail, name='Muju_detail'),
]