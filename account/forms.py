from django import forms
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm
from .models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = '__all__'

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        email = self.cleaned_data["email"]
        user.username = email
        random_password = MyUser.objects.make_random_password()
        user.should_change_password = True
        user.set_password(random_password)
        if commit:
            user.save()

        send_email(email, random_password)
        return user


class PasswordChangeForm(BasePasswordChangeForm):
    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        self.user.should_change_password = False
        if commit:
            self.user.save()
        return self.user


def send_email(to_email, password):
    subject = "Account Creation in KM Portal"
    message = "Account creation. Username: {} Default Password: {}".format(to_email, password)
    send_mail(subject, message, 'kmportaldev@gmail.com', [to_email], fail_silently=False)

