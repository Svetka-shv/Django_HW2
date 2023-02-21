from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from task.models import Task
from django.http import Http404


def task_list_view(request: HttpRequest):
    ctx ={
        "object_list": Task.objects.order_by("category"),
    }
    return render(request, 'task_list.html', ctx)

def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        raise Http404
    ctx = {
        "object": task,
    }
    return render(request, 'task_detail.html', ctx)

def category_view(request: HttpRequest, category) -> HttpResponse:
    ctx = {
        "object_category": Task.objects.filter(category=category)
    }
    return render(request, 'category.html', ctx)
