from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('add/', views.addbook, name='book-add'),
    path('update/<str:pk>', views.updatebook, name='book-update'),
]