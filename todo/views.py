from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import todo
from .serializer import TodoSerializer
from rest_framework.decorators import api_view
# Create your views here.
#CRUD
@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)

        return Response(todo_serializer.data, status.HTTP_200_OK)

    elif request.method =='POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


    return Response(None, status.HTTP_400_BAD_REQUEST)  

@api_view(['GET', 'PUT', 'DELETE'])
def tidi_detail_view(request:Request, todo_id:int):
    try:
        Todo = todo.objects.get(pk=todo_id)
    except todo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = TodoSerializer(Todo)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(Todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)