from django.shortcuts import render, redirect

from .models import Tasks
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {
        "tasks": tasks,
        "form": form,
    }
    return render(request, "tasks/list.html", context)

