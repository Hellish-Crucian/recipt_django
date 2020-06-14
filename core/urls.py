from django.urls import path

from . import views

urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('detail/<int:pk>', views.ResiptDetailView.as_view(), name='detail')
]