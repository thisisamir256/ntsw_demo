from django.urls import path
from .views import OverSeasSuplierListView, PersonCreateView, CompanyCreateView

app_name = 'supplier'

urlpatterns = [
    path('', OverSeasSuplierListView.as_view(), name='supplier_list'),
    path('create-person', PersonCreateView.as_view(), name='create_person'),
    path('create-company', CompanyCreateView.as_view(), name='create_company'),
]
