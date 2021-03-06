from rest_framework import serializers 
from apps.shipments.models import Shipments
 
 
class ShipmentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Shipments
        fields = ('id',
          'shipper_company_id',
          'carrier_company_id',
          'truck_id',
          'co2_model_id',
          'travelled_distance',
          'fuel_consumed',
          'estimated_fuel_consumed',
          'weight',
          'type_of_goods',
          'start_country',
          'start_city',
          'start_postcode',
          'end_country',
          'end_city',
          'end_postcode',
          'type_of_calculations',
          'allocated_distance',
          'allocated_fuel',
          'total_co2_emitted',
          'creation_timestamp',
          'last_updated_timestamp',
          'start_time',
          'end_time',
          'fuel_type')