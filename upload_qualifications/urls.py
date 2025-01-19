from django.urls import path

from .views import BusinessCardListView, BusinessCardCreateView


app_name = 'upload_qualifications'

urlpatterns = [
    path("business-cards/", BusinessCardListView.as_view(), name="business_cards"),
    path('create-business-card', BusinessCardCreateView.as_view(),
         name="create_business_card"),
    path('create-business-card/<str:active>', BusinessCardCreateView.as_view(),
         name="create_business_card"),

]
