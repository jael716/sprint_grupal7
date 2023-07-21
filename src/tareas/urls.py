from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import TareaListView, TareaDetailView, TareaUpdateView,TareaDeleteView,completar_tarea


urlpatterns = [
    path('', views.welcome, name='home'),
    path('tareas/', TareaListView.as_view(), name='lista_tarea'),
    path('tareas/<int:pk>/', TareaDetailView.as_view(), name='tarea_detail'),    
    path('tareas/crear/', views.tarea_crear, name='tarea_crear'),
    path('tareas/editar/<int:pk>/', TareaUpdateView.as_view(), name='tarea_editar'),
    path('tareas/borrar/<int:pk>/', TareaDeleteView.as_view(), name='tarea_borrar'),
    path('tareas/completar/<int:pk>/', completar_tarea, name='tarea_completar'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
