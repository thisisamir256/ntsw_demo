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
        print('1')
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        print('2')
        current_site = get_current_site(self.request)
        message = render_to_string('sms.txt',{
            'otp':12334
        })
        print('3')
        to_email = form.cleaned_data.get('email')
        to_mobile = form.cleaned.data.get('mobile')
        print(to_email)
        email = EmailMessage(
            'sms email', message, to=[to_email]
        )
        print(to_email)
        email.send()
        print('ok')
        return HttpRequest('regster seccessfull')

