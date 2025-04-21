from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StaffUser

@login_required
def user_profile(request):
    staff = StaffUser.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'staff': staff})
