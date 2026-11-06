from django.urls import path

from .forms import CommentForm
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, RegisterView, CommentCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(),name='task_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(),name='task_delete'),
    path('accounts/register/', RegisterView.as_view(),name='register'),
    path('task/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment')
]