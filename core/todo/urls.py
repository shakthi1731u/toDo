
# todo/urls.py
from django.urls import  path
from .views import  *


urlpatterns = [

    path('', TodoListView, name='todo-list'),
    path('todo/<int:pk>/', todo_detail_view, name='todo-detail'),
    path('todo/create/', todo_create_view, name='todo-create'),
    path('todo/<int:pk>/update/', todo_update_view, name='todo-update'),
    path('todo/<int:pk>/delete/', todo_delete_view, name='todo-delete'),
    path('todo/<int:pk>/toggle-complete/', todo_toggle_complete_view, name='todo-toggle-complete'),
]
