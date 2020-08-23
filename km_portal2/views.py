from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def dashboard(request):
    if request.user.should_change_password:
        return redirect('password_change')
    return render(request,
                  'dashboard/dashboard.html',
                  {'section': 'dashboard'})
