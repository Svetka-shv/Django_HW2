from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404

# Create your views here.

tasks = [{"id": 1, "title": "Task #1", "description": "Some long task description", "created": "2022-01-24 12:00", "updated": "2022-01-25 12:00", "completed": False},
    {"id": 2, "title": "Task #2", "description": "Some long task description", "created": "2022-01-24 12:00", "updated": "2022-01-25 12:00", "completed": True},
    {"id": 3, "title": "Task #3", "description": "Some long task description", "created": "2022-01-24 12:00", "updated": "2022-01-25 12:00", "completed": False},
    {"id": 4, "title": "Task #4", "description": "Some long task description", "created": "2022-01-24 12:00", "updated": "2022-01-25 12:00", "completed": True},
    {"id": 5, "title": "Task #5", "description": "Some long task description", "created": "2022-01-24 12:00", "updated": "2022-01-25 12:00", "completed": False}
]


def task_list_view(request: HttpRequest):
    return render(request, 'task_list.html', {"tasks": tasks})

def task_detail_view(request: HttpRequest, id: int) -> HttpResponse:
    for task in tasks:
        if task["id"] == id:
            return render(request, 'task_detail.html', {"task": task})
    raise Http404
