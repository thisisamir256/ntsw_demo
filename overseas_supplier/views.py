from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from itertools import chain
from operator import attrgetter

from .models import Person, Company
from .forms import PersonCreationForm, CompanyForm

User = get_user_model()


class OverSeasSuplierListView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        p_q = Person.objects.filter(user=user)
        c_q = Company.objects.filter(user=user)
        combined = sorted(
            chain(p_q, c_q),
            key=attrgetter('created_at'),
            reverse=True  # برای مرتب‌سازی نزولی
        )

        return render(request, 'overseas_supplier/list.html', {'combined': combined})


class PersonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PersonCreationForm
    model = Person
    template_name = "overseas_supplier/partials/person_form.html"
    success_url = reverse_lazy('supplier:supplier_list')
    success_message = 'فروشنده‌ی شما با موفقیت ایجاد شد'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success_url': self.success_url})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form_context = render_to_string(
                'overseas_supplier/partials/person_form.html', {'form': form}, request=self.request)
            return HttpResponse(form_context, status=400)
        return super.form_invalid(form)


class CompanyCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "overseas_supplier/partials/company_form.html"
    success_url = reverse_lazy('supplier:supplier_list')
    success_message = 'شناسه‌ی فروشنده‌ی خارجی شما با موفقیت صادر گردید'
    form_class = CompanyForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success_url': self.success_url})
        return super.form_invalid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form_context = render_to_string(
                'overseas_supplier/partials/company_form.html', {'form': form}, request=self.request)
            return HttpResponse(form_context, status=400)
        return super.form_invalid(form)
