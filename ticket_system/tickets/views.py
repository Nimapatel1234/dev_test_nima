from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import StaffUser
from .models import Ticket, Attachment
from django.http import HttpResponse

# Ticket Dashboard
@login_required
def ticket_dashboard(request):
    if request.user.is_staff:  # Admin User
        tickets = Ticket.objects.all()
    else:  # Staff User
        tickets = Ticket.objects.filter(assigned_to=request.user)

    # Ticket Counts
    draft_count = tickets.filter(status='Draft').count()
    ongoing_count = tickets.filter(status='Ongoing').count()
    completed_count = tickets.filter(status='Completed').count()

    context = {
        'tickets': tickets,
        'draft_count': draft_count,
        'ongoing_count': ongoing_count,
        'completed_count': completed_count,
    }
    return render(request, 'tickets/ticket_dashboard.html', context)

# Update Ticket Status
@login_required
def update_ticket_status(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    try:
        staff = StaffUser.objects.get(user=request.user)
    except StaffUser.DoesNotExist:
        return HttpResponse('You are not a staff user.', status=403)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        uploaded_files = request.FILES.getlist('files')  # ✅ Get list of files

        # Allowed Status Changes
        if staff.is_admin:
            allowed_statuses = ['draft', 'ongoing', 'completed', 'archived']
        else:
            allowed_statuses = ['ongoing', 'completed']

        if new_status in allowed_statuses:
            ticket.status = new_status
            ticket.save()

        # Save uploaded attachments
        for file in uploaded_files:  # ✅ Loop through files
            Attachment.objects.create(ticket=ticket, file=file)

        return redirect('user_profile')  # or 'tickets:ticket_dashboard'

    return render(request, 'tickets/update_ticket_status.html', {'ticket': ticket})
