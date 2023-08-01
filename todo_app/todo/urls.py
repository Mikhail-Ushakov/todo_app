from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path('edit/<int:pk>/', views.TaskEdit.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),
    path('change-status/<int:pk>/', views.change_status, name='change-status'),
]