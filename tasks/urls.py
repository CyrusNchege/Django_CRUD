from django.urls import path
from . import views

app_name='tasks'

urlpatterns = [
    path('', views.task_list, name = 'task_list'),
    path('<int:id>', views.task_detail, name='task_details'),
    path('create/', views.create_task, name = 'create_task'),
    path('<int:id>/delete', views.delete_task, name='delete_task'),
    path('<int:id>/update', views.update_task, name = 'update_task')

]