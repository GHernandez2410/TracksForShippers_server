from django.shortcuts import render
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from apps.shipments.models import Shipments
from apps.shipments.serializers import ShipmentSerializer
from rest_framework.decorators import api_view

import ipdb

@api_view(['GET'])
def getAndFilterShipments_list(request):
    if request.method == 'GET':
        shipments = Shipments.objects.all()
        
        # User can filter by 
        # Type of calculation =>  type_of_calculations
        # Goods type => type_of_goods
        # Start City => start_city
        # End City => end_city

        # User can select any start and end perid  dates

        type_of_calculations = request.GET.get('type_of_calculations', None)
        type_of_goods = request.GET.get('type_of_goods', None)
        start_city = request.GET.get('start_city', None)
        end_city = request.GET.get('end_city', None)
        start_time = request.GET.get('start_time', None)
        end_time = request.GET.get('end_time', None)

        if type_of_calculations is not None:
            shipments = shipments.filter(type_of_calculations__icontains=type_of_calculations)
        if type_of_goods is not None:
            shipments = shipments.filter(type_of_goods__icontains=type_of_goods)
        if start_city is not None:
            shipments = shipments.filter(start_city__icontains=start_city)
        if end_city is not None:
            shipments = shipments.filter(end_city__icontains=end_city)
            
        if start_time is not None:
            shipments = shipments.filter(start_time__range=(start_time, start_time))
        if end_time is not None:
            shipments = shipments.filter(end_time__range=(end_time, end_time))

        shipments_serializer = ShipmentSerializer(shipments, many=True)
        return JsonResponse(shipments_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 