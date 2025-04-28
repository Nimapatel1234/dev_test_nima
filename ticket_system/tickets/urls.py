from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.ticket_dashboard, name='ticket_dashboard'),
    path('ticket/<int:ticket_id>/update/', views.update_ticket_status, name='update_ticket_status'),
]
