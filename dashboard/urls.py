from django.urls import path
from .views import BaseRoleView, BusinessRoleView


app_name = 'dashboard'

urlpatterns = [
    path('base/', BaseRoleView.as_view(), name='base_role_dashboard'),
    path('business/', BusinessRoleView.as_view(),
         name="business_role_dashboard"),
]
