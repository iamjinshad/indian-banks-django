from django.shortcuts import render, redirect
from django.conf import settings

# Rest packages
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

# Models
from .models import *

# packages
import csv 
import string



@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def Fetch_Bank_Details_Using_Ifsc(request):
	ifsc 			= request.data.get("ifsc")
	bank    		= branches.objects.filter(ifsc=ifsc).values('bank__name','ifsc','branch','address','city','district','state','bank__id')
	return Response({"code": "200", 'message': "success","bank":bank, "Response": True},
					status=HTTP_200_OK)



@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def Fetch_Bank_Details_Using_City_And_Bank_Aame(request):
	city 				= request.data.get("city")
	bank_name 			= request.data.get("bank_name")
	offset		 		= int(request.GET.get('offset' ,'1'))
	limit		 		= int(request.GET.get('limit' ,'10'))
	limit 				= limit + offset
	branche 			= branches.objects.filter(city__icontains=city,bank__name__icontains=bank_name).values('id','branch','bank__name','ifsc','address','city','district','state','bank__id')[offset:limit]
	return Response({"code": "200", 'message': "success","branches":branche, "Response": True},
					status=HTTP_200_OK)



def decode_utf8(input_iterator):
	for l in input_iterator:
		yield l.decode('utf-8')



def Csv_Upload(request):
	if request.method == 'POST':
		reader = csv.DictReader(decode_utf8(request.FILES['csv_file']))
		count = 0
		for row in reader:
			count += 1
			if count == 50:
				break
			if settings.DEBUG:
				print('=============================================----')
				# data = banks(name=row['bank_name'], _id=row['bank_id'])
				# data.save()
				# branches(bank=data, ifsc=row['ifsc'], branch=row['branch'], address=row['address'], city=row['city'], district=row['district'], state=row['state']).save()
		return redirect('csv_upload')
	else:
		return render(request, 'csv_upload.html')







