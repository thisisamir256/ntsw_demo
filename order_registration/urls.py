from django.urls import path

from .views import MainDataCreateView

app_name = 'order_registration'

urlpatterns = [
    path('main-data-create', MainDataCreateView.as_view(), name='main_data_create')
]
