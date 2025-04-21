

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import StaffUser
from .models import Ticket, Attachment

@login_required
def ticket_dashboard(request):
    staff = StaffUser.objects.get(user=request.user)
    tickets = Ticket.objects.all() if staff.is_admin else Ticket.objects.filter(assigned_to=staff)

    context = {
        'user': staff,
        'tickets': tickets,
        'draft_count': tickets.filter(status='draft').count(),
        'ongoing_count': tickets.filter(status='ongoing').count(),
        'completed_count': tickets.filter(status='completed').count(),
    }
    return render(request, 'tickets/dashboard.html', context)

@login_required
def update_ticket_status(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    staff = StaffUser.objects.get(user=request.user)

    if request.method == "POST":
        new_status = request.POST.get("status")
        file = request.FILES.get("file")

        # Role-based allowed status transitions
        if staff.is_admin:
            allowed_statuses = ['draft', 'ongoing', 'completed', 'archived']
        else:
            allowed_statuses = ['ongoing', 'completed']

        if new_status in allowed_statuses:
            ticket.status = new_status
            ticket.save()

        # Handle file upload
        if file:
            Attachment.objects.create(ticket=ticket, file=file)

        return redirect('ticket_dashboard')

    return render(request, 'tickets/update_ticket.html', {'ticket': ticket, 'user': staff})
