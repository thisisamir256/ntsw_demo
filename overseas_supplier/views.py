from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model

from .models import Person, Company
User = get_user_model()


class OverSeasSuplierListView(View):
    def get(self, request):
        user = request.user
        p_q = Person.objects.filter(user=user)
        c_q = Company.objects.filter(user=user)
        context = {
            'person': p_q,
            'company': c_q,
        }
        return render(request, 'overseas_suplier/list.html', context)
