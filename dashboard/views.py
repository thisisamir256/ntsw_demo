from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseRoleView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user.active_role = 'br'
        user.save()
        return render(request, 'dashboard/base_role_index.html')


class BusinessRoleView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user.active_role = 'bc'
        user.save()
        print(user.active_role)
        return render(request, 'dashboard/business_role_index.html')


class TraderRoleView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user.avtive_role = 'it'
        user.save()
        return render(request, 'dashboard/trader_role_index.html')
