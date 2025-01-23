from django.urls import path
from .views import OverSeasSuplierListView, PersonCreateView

app_name = 'supplier'

urlpatterns = [
    path('', OverSeasSuplierListView.as_view(), name='supplier_list'),
    path('create-person', PersonCreateView.as_view(), name='create_person'),
    path('create-company', PersonCreateView.as_view(), name='create_company'),
]
