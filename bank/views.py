from django.shortcuts import render, redirect
import csv 

from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.template import RequestContext
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *




@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def fetch_bank_details_using_ifsc(request):
	ifsc 			= request.data.get("ifsc")
	bank    		= branches.objects.filter(ifsc=ifsc).values('bank__name','ifsc','branch','address','city','district','state','bank__id')
	return Response({"code": "200", 'message': "success","bank":bank, "Response": True},
					status=HTTP_200_OK)



@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def fetch_bank_details_using_city(request):
	city 				= request.data.get("city")
	bank_name 			= request.data.get("bank_name")
	page		 		= request.GET.get('page' ,'1')
	limit 				= 10 * int(page)
	offset 				= limit - 10
	branche 			= branches.objects.filter(city__icontains=city,bank__name__icontains=bank_name).values('branch')[offset:limit]
	return Response({"code": "200", 'message': "success","branches":branche, "Response": True},
					status=HTTP_200_OK)




class HelloView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		content = {'message': 'Hello, World!'}
		return Response(content)
	 






def csv_upload(request):
	if request.method == 'POST':
		csv_file 		= request.FILES['csv_file']


	 #    for x in f:
	 #        if x.startswith('newick;'):
	 #            print('')

		# with open(csv_file, newline='') as csvfile:
		# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		# 	for row in spamreader:
		# 		print(', '.join(row)) 

		return redirect('csv_upload')
	else:
		return render(request, 'csv_upload.html')





