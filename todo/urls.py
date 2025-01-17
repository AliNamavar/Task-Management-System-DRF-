from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_todos, name='serialize_todos'),
    path('<int:todo_id>', views.tidi_detail_view, name='put_delete_view')
]