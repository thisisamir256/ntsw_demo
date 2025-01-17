from django.contrib.auth.views import LogoutView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from persiantools.jdatetime import JalaliDate
from persiantools.jdatetime import JalaliDateTime

class LogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    
    def form_valid(self, form):
        print('1')
        user = form.save(commit=False)
        user.is_active = False
        user.username = form.cleaned_data.get('national_code')
        birthday = form.cleaned_data.get('birthday')
        print(birthday)
        birthday_list = birthday.split('/')
        user.birth_date = JalaliDate(int(birthday_list[0]),int(birthday_list[1]),int(birthday_list[2])).to_gregorian()
        print('user is', user.birth_date)
        user.save()
        print('2')
        message = render_to_string('users/sms.txt',{
            'otp':12334
        })
        print('3')
        to_email = form.cleaned_data.get('email')
        to_mobile = form.cleaned_data.get('mobile')
        print(to_email)
        if to_email:
            email = EmailMessage(
                'sms email', message, to=[to_email]
            )
            email.send()
        print(to_email)
        print('ok')
        return HttpRequest('regster seccessfull')

