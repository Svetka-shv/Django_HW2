"""
Task application URL Configuration
"""

from django.urls import path
from task.views import task_list_view, task_detail_view, category_view

urlpatterns = [
    path("", task_list_view, name="task-list"),
    path("<int:pk>/", task_detail_view, name="task-detail"),
    path("<str:category>/", category_view, name="category-view")
]