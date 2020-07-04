from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('publish/', views.publish, name='publish'),
    path('edit/', views.edit, name='edit'),
    path('my/', views.my, name='my'),
    path('delete/<int:identity>/', views.delete, name='delete'),
    path('user/<int:identity>/', views.user, name='user'),
]
