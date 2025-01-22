from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Person, Company
from .forms import PersonCreationForm
User = get_user_model()


class OverSeasSuplierListView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        p_q = Person.objects.filter(user=user)
        c_q = Company.objects.filter(user=user)
        person_creation_form = PersonCreationForm()
        context = {
            'person_form': person_creation_form,
            'person': p_q,
            'company': c_q,
        }
        return render(request, 'overseas_supplier/list.html', context)


class PersonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Person
    fields = (
        'first_name',
        'last_name',
        'father_name',
        'mother_name',
        'grandfather_name',
        'country',
        'city',
        'gender',
        'birthday',
        'nationality',
        'maried',
        'personal_image',
        'document_type',
        'document_number',
        'issue_date',
        'expire_date',
    )
    template_name = "overseas_supplier/partials/person_form.html"
    success_url = reverse_lazy('supplier:supplier_list')
    success_message = 'فروشنده‌ی شما با موفقیت ایجاد شد'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)

    def form_invalid(self, form):
        form_context = render_to_string(
            'overseas_supplier/partials/person_form.html', {'form': form})
        return HttpResponse(form_context, status=400)
