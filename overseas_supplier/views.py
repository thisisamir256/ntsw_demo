from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model

from .models import Person, Company
User = get_user_model()


class OverSeasSuplierListView(View):
    def get(self):
        p_q = Person.objects.filter()
