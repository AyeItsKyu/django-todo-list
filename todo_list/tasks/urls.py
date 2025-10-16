from django.urls import path
from .views import CustomLoginView, TasksListView, AddTask, EditTask, DeleteTask
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TasksListView.as_view(), name='tasks'),
    path('tasks/add/', AddTask.as_view(), name='add_task'),
    path('tasks/edit/<int:id>', EditTask.as_view(), name='edit_task'),
    path('task/delete/<int:id>', DeleteTask.as_view(), name='delete_task'),
]