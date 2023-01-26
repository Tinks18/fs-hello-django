
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, add_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name='get_todo_list'),
    path('add', add_item, name='add'),
]
