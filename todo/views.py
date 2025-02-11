from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import todo
from .serializer import TodoSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
# Create your views here.

User = get_user_model()
#region function views\


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

#endregion

#region class base views

class TodosListApi(APIView):
    @extend_schema(
        request=TodoSerializer,
        responses={201: TodoSerializer},
    )
    def get(self, request:Request):
        todos = todo.objects.all()
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request:Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        

        return Response(None, status.HTTP_400_BAD_REQUEST)

class TodosDetailApiView(APIView):

    def get_todo(self, todo_id):
        try:
            todos = todo.objects.get(pk=todo_id)
            return todos
        except todo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)
        #todo:fox this


    def get(self, request:Request, todo_id:int):
        todos = self.get_todo(todo_id) 
        serializer = TodoSerializer(todos)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request:Request, todo_id):
        todos = self.get_todo(todo_id)
        serializer = TodoSerializer(todos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        
        return Response(None, status.HTTP_400_BAD_REQUEST)      
    
    def delete(self, request:Request, todo_id):
        todos = self.get_todo(todo_id)
        todos.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
    
#endregion

#region mixins

class TodoMixinsaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request:Request):
        return self.list(request)
    

    def post(self, request:Request):
        return self.create(request)

class TodoMixinsDetailApiView(mixins.RetrieveModelMixin ,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request:Request, pk):
        return self.retrieve(request, pk)


    def put(self, request:Request, pk):
        return self.update(request, pk)

    def delete(self, request:Request, pk):
        return self.destroy(request, pk)



#endregion

#region generics
class GenericsTodoPagination(PageNumberPagination):
    page_size = 1


class TodoGenericsApiView(generics.ListCreateAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = GenericsTodoPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    

class TodoGenericsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer
    
#endregion

#region viewsets

class TodoViewSetsApi(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = LimitOffsetPagination


#endregion

#region user
class UserGenericsList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

#endregion