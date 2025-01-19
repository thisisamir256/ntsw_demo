from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UsernameForm, PasswordResetForm
from .models import VerificationCode
from django.views.generic import CreateView, TemplateView, View, FormView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib import messages


from persiantools.jdatetime import JalaliDate
from persiantools.jdatetime import JalaliDateTime
from persiantools import digits

from decouple import config
import uuid


User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.username = form.cleaned_data.get('national_code')
        birthday = form.cleaned_data.get('birthday')
        print(birthday)
        birthday_list = birthday.split('/')
        user.birth_date = JalaliDate(int(birthday_list[0]), int(
            birthday_list[1]), int(birthday_list[2])).to_gregorian()
        user.save()
        return redirect('users:select_verification_mod', user_uuid=str(user.uuid))


class SelectVerificationMod(View):
    def get(self, request, user_uuid, *args, **kwargs):
        user = get_object_or_404(User, uuid=user_uuid)
        return render(request, 'users/select_verification_mod.html', {'user_uuid': user_uuid})


class VerifyPhoneView(FormView):

    def get(self, request, user_uuid, *args, **kwargs):
        code = 1111
        user = get_object_or_404(User, uuid=user_uuid)
        verification_codes = VerificationCode.objects.filter(
            user=user).order_by('created_at')
        verification_code = verification_codes.last()
        msg = 'کد تایید قبلا برای شما ارسال شده است. لطفا پس از اتمام سه دقیقه از آخرین ارسال کد تایید دوباره درخواست دهید.'
        if not verification_codes or not verification_code.is_valid:
            msg = 'کد اعتبار سنجی برای تلفن همراه شما ارسال گردید، لطفا پس از دریافت در کادر زیر وارد نمایید.'
            verification_code = VerificationCode.objects.create(
                verification_code=code,
                user=user
            )
        # todo: SEND SMS
        context = {
            'msg': msg,
            'user_uuid': user_uuid,
            'uuid': verification_code.uuid,
            'time_turtling': config('SMS_TIME_TURTLING', cast=int, default=3),
        }
        return render(request, 'users/verify_phone.html', context)

    def post(self, request, user_uuid, *args, **kwargs):
        uuid_str = request.POST.get('uuid')
        verification_cod_uuid = uuid.UUID(uuid_str)
        verification = get_object_or_404(
            VerificationCode, uuid=verification_cod_uuid)
        code = request.POST.get('verification_code')
        code = digits.fa_to_en(code)

        # بررسی کد تأیید
        if str(verification.verification_code) == code:
            if verification.is_valid:
                user = verification.user
                user.is_active = True
                user.is_mobile_verified = True
                user.save()
                messages.success(
                    self.request, "شماره موبایل شما با موفقیت تایید شد")
                return redirect('users:login')
            else:
                return HttpResponse("کد تأیید منقضی شده است.")
        else:
            return HttpResponse("کد تأیید اشتباه است.")


class SendResetCodeView(FormView):
    template_name = 'users/send_reset_code.html'
    form_class = UsernameForm
    success_url = reverse_lazy('users:password-reset-confirm')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        user = get_object_or_404(User, username=username)
        code = 1111
        # تولید کد تأیید
        # code = str(random.randint(1000, 9999))
        # todo: SEND SMS

        verification_code = VerificationCode.objects.create(
            user=user, verification_code=code)

        # ارسال پیامک (چاپ برای آزمایش)
        print(f"کد تأیید برای {user.username}: {code}")

        return redirect('users:password_reset_confirm', verification_uuid=verification_code.uuid)


class ResetPasswordView(FormView):
    template_name = 'users/reset_password.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        code = digits.fa_to_en(form.cleaned_data['code'])
        new_password = form.cleaned_data['new_password']

        # بازیابی کاربر از UUID
        # user_uuid = uuid.UUID(self.kwargs.get('user_uuid'))
        verification_code_uuid = self.kwargs.get('verification_uuid')
        verification_code = get_object_or_404(
            VerificationCode, uuid=verification_code_uuid)
        user = verification_code.user

        # بررسی کد تأیید
        if not verification_code or not verification_code.is_valid or code != verification_code.verification_code:
            messages.error(self.request, "کد تأیید نامعتبر یا منقضی شده است.")
            return redirect('users:send_reset_code')  # هدایت به صفحه ارسال کد

        user.set_password(new_password)  # تغییر رمز عبور
        user.save()
        messages.success(self.request, "رمز عبور با موفقیت تغییر یافت.")
        return redirect('users:login')


# message = render_to_string('users/sms.txt',{
#             'otp':12334
#         })
#         print('message is: ', message)
#         verification_code = random.randint(1000, 9999)
#         verification = VerificationCode.objects.create(
#             user=user,
#             verification_code=verification_code,
#         )
#         to_mobile = form.cleaned_data.get('mobile')
