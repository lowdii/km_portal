from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from .forms import PasswordChangeForm

@login_required
def dashboard(request):
    if request.user.should_change_password:
        return redirect('password_change')
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


class PasswordChangeView(BasePasswordChangeView):
    form_class = PasswordChangeForm
