from django.contrib import admin
from .models import Todo

# Register your models here.

def register_todo_model():
    from .models import Todo
    admin.site.register(Todo)
    


def unregister_todo_model():
    from .models import Todo
    admin.site.unregister(Todo)
    



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    list_editable = ('completed',)