from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnProjects, name="projects"),
    path('project/<int:pid>', views.returnProject, name="project"),
]
