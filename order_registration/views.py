from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MainDataForm
from django.urls import reverse_lazy


class MainDataCreateView(LoginRequiredMixin, CreateView):
    form_class = MainDataForm
    template_name = 'order_registration/create_main_data.html'
    success_url = reverse_lazy('users:login')
