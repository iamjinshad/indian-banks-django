from django.urls import path
from .views import *


urlpatterns = [
 
    path('csv_upload', Csv_Upload, name='csv_upload'),
    path('', Fetch_Bank_Details_Using_Ifsc, name='fetch_bank_details_using_ifsc'),
    path('bank-branches', Fetch_Bank_Details_Using_City_And_Bank_Aame, name='fetch_bank_details_using_city_and_bank_name'),
    
]
