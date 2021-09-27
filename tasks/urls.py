from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>/', views.updateTask, name='update'),
    path('delete/<int:id>/', views.deleteTask, name='delete'),
]