from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import StaffUser

@login_required
def user_profile(request):
    staff = StaffUser.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'staff': staff})

# ✅ Logout View
@login_required
def user_logout(request):
    logout(request)  # Django built-in logout
    return redirect('login')  # Redirect to Login page after logout
