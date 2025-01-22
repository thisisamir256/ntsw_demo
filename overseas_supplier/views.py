from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

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
        
    )
    template_name = "overseas_supplier.html"
    success_url = reverse_lazy('supplier:supplier_list')
    success_message = 'فروشنده‌ی شما با موفقیت ایجاد شد'

    def form_invalid(self, form):
        return reverse_lazy('supplier:supplier_list')
