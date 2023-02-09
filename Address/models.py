# from django.db import models
# from smart_selects.db_fields import ChainedForeignKey


# class Country(models.Model):
#     country = models.CharField(max_length=255)

#     class Meta:
#         db_table= "country"

#     def __str__(self):
#        return self.country

# class State(models.Model):
#     country = models.ForeignKey('Country', on_delete = models.CASCADE)
#     state = models.CharField(max_length=255)


#     class Meta:
#         db_table= "state"

#     def __str__(self):
#        return self.state

# class City(models.Model):
#     city = models.CharField(max_length=255,verbose_name="city")
#     country = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
    
#     class Meta:
#         db_table= "city"

#     def __str__(self):
#        return self.city

from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Country(models.Model):
    country = models.CharField(max_length=255)

    class Meta:
        db_table= "country"

    def __str__(self):
       return self.country

class State(models.Model):
    country = models.ForeignKey('Country', on_delete = models.CASCADE)
    state = models.CharField(max_length=255)


    class Meta:
        db_table= "state"

    def __str__(self):
       return self.state

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = ChainedForeignKey(State,chained_field="country",chained_model_field="country",show_all=False,auto_choose=True,sort=True)
    city = models.CharField(max_length=255,verbose_name="city")


    class Meta:
        db_table= "city"

    def __str__(self):
       return self.city
