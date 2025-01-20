from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from persiantools.jdatetime import JalaliDateTime

from .models import BusinessCard
from datetime import datetime
from urllib.parse import urlencode

User = get_user_model()


class BusinessCardCreateView(LoginRequiredMixin, CreateView):
    model = BusinessCard
    fields = []

    def get_success_url(self):
        base_url = reverse_lazy(
            'upload_qualifications:business_cards')
        query_params = {'active': 'bazorgan'}
        return f"{base_url}?{urlencode(query_params)}"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)

    def form_invalid(self, form):
        return 'amir'


class BusinessCardListView(LoginRequiredMixin, ListView):
    model = BusinessCard
    template_name = "upload_qualifications/business_card_list.html"

    def get_queryset(self):
        q = super().get_queryset()
        return q.filter(user=self.request.user)
