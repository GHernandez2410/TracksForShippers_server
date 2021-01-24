from django.db import models

class Shipments(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    shipper_company_id = models.IntegerField(blank=True, null=True)
    carrier_company_id = models.IntegerField(blank=True, null=True)
    truck_id = models.IntegerField(blank=True, null=True)
    co2_model_id = models.IntegerField(blank=True, null=True)
    travelled_distance = models.FloatField(blank=True, null=True)
    fuel_consumed = models.FloatField(blank=True, null=True)
    estimated_fuel_consumed = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    type_of_goods = models.CharField(max_length=128, blank=True, null=True)
    start_country = models.CharField(max_length=128, blank=True, null=True)
    start_city = models.CharField(max_length=128, blank=True, null=True)
    start_postcode = models.CharField(max_length=128, blank=True, null=True)
    end_country = models.CharField(max_length=128, blank=True, null=True)
    end_city = models.CharField(max_length=128, blank=True, null=True)
    end_postcode = models.CharField(max_length=128, blank=True, null=True)
    type_of_calculations = models.CharField(max_length=128, blank=True, null=True)
    allocated_distance = models.FloatField(blank=True, null=True)
    allocated_fuel = models.FloatField(blank=True, null=True)
    total_co2_emitted = models.FloatField(blank=True, null=True)
    creation_timestamp = models.DateTimeField(blank=True, null=True)
    last_updated_timestamp = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    fuel_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipments'