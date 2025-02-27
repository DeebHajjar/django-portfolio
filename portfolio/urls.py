from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pid>', views.project_detail, name='project_detail'),
    path('project/<int:pid>/rate/', views.rate_project, name='rate_project')
]
