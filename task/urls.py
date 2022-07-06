from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createtask, name='createtask'),
    path('current/', views.currenttasks, name='currenttasks'),
    path('completed/', views.completedtasks, name='completedtasks'),
    path('task/<int:task_pk>', views.viewtask, name='viewtask'),
    path('task/<int:task_pk>/complete', views.completetask, name='completetask'),
    path('task/<int:task_pk>/delete', views.deletetask, name='deletetask'),
]
