from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MainDataForm


class MainDataCreateView(LoginRequiredMixin, CreateView):
    form_class = MainDataForm
    template_name = 'order_registration/create_main_data.html'
