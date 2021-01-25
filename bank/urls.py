from django.urls import path
from .views import *




urlpatterns = [
 
    path('', csv_upload, name='csv_upload'),
    path('bank-details-ifsc/', fetch_bank_details_using_ifsc, name='bank_details'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('bank-details-city/', fetch_bank_details_using_city, name='bank_details'),
    
]
