from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import TaskForm, CommentForm
from .models import Task, Comment

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'taskmanager/task_list.html'
    context_object_name = 'my_tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskmanager/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskmanager/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskmanager/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'taskmanager/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'taskmanager/task_comment.html'
    success_url = reverse_lazy('task')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)