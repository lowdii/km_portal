from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from .forms import PasswordChangeForm


class PasswordChangeView(BasePasswordChangeView):
    form_class = PasswordChangeForm


