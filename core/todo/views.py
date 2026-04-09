# todo/views.py
from django.shortcuts import get_object_or_404, redirect, render


from .models import Todo

# Create your views here.
def TodoListView(request):
    
    from .models import Todo
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail_view(request, pk):
    from .models import Todo
    todo = Todo.objects.get(pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'

        Todo.objects.create(
            title=title,
            description=description,
            completed=completed
        )
        return redirect('todo-list')

    return render(request, 'todo/todo_create.html')


def todo_update_view(request, pk):
    from .models import Todo
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
    return render(request, 'todo/todo_update.html', {'todo': todo})


def todo_delete_view(request, pk):
    from .models import Todo
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
    return render(request, 'todo/todo_delete.html', {'todo': todo})



def todo_toggle_complete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.toggle_complete()
    return redirect('todo-list')