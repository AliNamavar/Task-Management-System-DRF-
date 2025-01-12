from django.shortcuts import render
from todo.models import todo
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def index_page(request):
    context = {
        'todos': todo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)


@api_view(['GET'])
def index_Json(request: Request):
    todos = list(todo.objects.order_by('priority').all().values('title', 'is_done'))

    return Response({
        'todos': todos
    },
    status.HTTP_200_OK) 