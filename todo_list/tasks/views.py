from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from .models import Task
from .form import TaskForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('tasks')

class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context
    
class AddTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_edit.html"
    success_url = reverse_lazy("tasks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mode"] = "Add"
        context["task"] = ""
        return context
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/task_edit.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = "Edit"
        return context
    
class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'Delete'
        return context