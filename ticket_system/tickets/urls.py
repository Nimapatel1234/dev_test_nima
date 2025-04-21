from django.urls import path
from . import views

urlpatterns = [
    path('/ticket', views.ticket_dashboard, name='ticket_dashboard'),
    path('ticket/<int:pk>/update/', views.update_ticket_status, name='update_ticket'),
]
