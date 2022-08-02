from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('add/', views.addbook, name='book-add'),
    path('update/<str:pk>', views.updatebook, name='book-update'),
    path('delete/<str:pk>', views.deletebook, name='book-delete'),
    path('/reserve/delete/<str:pk>', views.deletereservebook, name='book-reserve-delete'),
    path('books/', views.viewbooks, name='book-view'),
    path('reservebooks/', views.reservebooks, name='book-reserve'),
    path('borrow/<str:pk>/', views.borrowbook, name='book-borrow'),
    path('return/<str:pk>/', views.returnbook, name='book-return'),
    path('book/details/<str:pk>/', views.bookdetails, name='book-details'),
]
