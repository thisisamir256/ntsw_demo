from django.urls import path
from .views import OverSeasSuplierListView, PersonCreateView

app_name = 'supplier'

urlpatterns = [
    path('', OverSeasSuplierListView.as_view(), name='supplier_list'),
    path('create', PersonCreateView.as_view(), name='create_supplier'),
]
