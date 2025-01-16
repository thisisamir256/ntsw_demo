from django.contrib.auth.views import LogoutView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string



class LogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        message = render_to_string('sms.txt',{
            'otp':12334
        })
        to_email = form.cleaned_data.get('email')
        to_mobile = form.cleaned.data.get('mobile')
        email = EmailMessage(
            'sms email', message, to=[to_email]
        )
        email.send()
        return HttpRequest('regster seccessfull')

