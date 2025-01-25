from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodoViewSetsApi)



urlpatterns = [
    path('', views.all_todos, name='serialize_todos'),
    path('<int:todo_id>', views.tidi_detail_view, name='put_delete_view'),
    path('cbv', views.TodosListApi.as_view(), name='cbv_G_P'),
    path('cbv/<int:todo_id>',views.TodosDetailApiView.as_view(),  name='cbv_P_D'),
    path('mixins', views.TodoMixinsaList.as_view(), name='mixinsTodoList'),
    path('mixins/<int:pk>', views.TodoMixinsDetailApiView.as_view(), name='mixinsTodoList'),
    path('generics/', views.TodoGenericsApiView.as_view(), name='GenericsApiView'),
    path('generics/<pk>', views.TodoGenericsDetailApiView.as_view(), name='GenericsApiView'),
    path('viewsets/', include(router.urls), name='ViewsetsUrls'),
    path('user', views.UserGenericsList.as_view(), name='UserGenerics'),



]