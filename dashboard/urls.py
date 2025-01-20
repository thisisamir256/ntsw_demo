from django.urls import path
from .views import BaseRoleView, BusinessRoleView, TraderRoleView


app_name = 'dashboard'

urlpatterns = [
    path('base/', BaseRoleView.as_view(), name='base_role_dashboard'),
    path('business/', BusinessRoleView.as_view(),
         name="business_role_dashboard"),
    path('trader/', TraderRoleView.as_view(), name='trader_role_dashbord')
]
