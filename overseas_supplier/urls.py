from django.urls import path
from .views import OverSeasSuplierListView

app_name = 'supplier'

urlpatterns = [
    path('', OverSeasSuplierListView.as_view(), name='supplier_list'),
]
