from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_todos, name='serialize_todos'),
    path('<int:todo_id>', views.tidi_detail_view, name='put_delete_view'),
    path('cbv', views.TodosListApi.as_view(), name='cbv_G_P'),
    path('cbv/<int:todo_id>',views.TodosDetailApiView.as_view(),  name='cbv_P_D'),


]