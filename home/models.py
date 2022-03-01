from tabnanny import verbose
from django.db import models

class Customer(models.Model):
    Policy_id = models.IntegerField()
    Date_of_Purchase = models.DateField()	
    Customer_id	= models.IntegerField()
    Fuel                    = models.CharField(max_length=20)
    VEHICLE_SEGMENT	        = models.CharField(max_length=10)
    Premium	                = models.IntegerField()
    bodily_injury_liability = models.IntegerField() 
    personal_injury_protection = models.IntegerField()	 
    property_damage_liability = models.IntegerField()	 
    collision               = models.IntegerField()	 
    comprehensive	        = models.IntegerField()
    Customer_Gender	        = models.CharField(max_length=20)
    Customer_Income_group   = models.CharField(max_length=20)
    Customer_Region	        = models.CharField(max_length=20)
    Customer_Marital_status = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name_plural = 'Customer details'
