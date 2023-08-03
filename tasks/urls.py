from django.urls import path
from .views import index, updateTask, delete

urlpatterns = [
    path("", index, name="list"),
    path("update-task/<str:pk>/", updateTask, name="update_task"),
    path("delete-task/<str:pk>/", delete, name="delete_task"),
]