from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('task/new/', views.new_task, name='new_task'),
    path('task/edit/<int:id>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:id>/', views.delete_task, name='delete_task'),
]
