from django.urls import path
from .views import index, projects ,tasks, registration, login_view, add_project
urlpatterns = [
	path('', index),
	path('my-projects', projects),
	path('my-tasks', tasks),
	path('registration', registration),
	path('login', login_view),
	path('add_project', add_project)
]
