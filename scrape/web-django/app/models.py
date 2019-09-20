from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class AreaData(models.Model):
    area_list = models.CharField(max_length=100)
    list_jpen = models.CharField(max_length=100, null=True)
    list_id = models.IntegerField(default=1)
    
    def __str__(self):
        return self.area_list


class StoreData(models.Model):
    store_area = models.ForeignKey(AreaData, on_delete = models.CASCADE)
    store_name = models.CharField(max_length=200)
    store_url = models.CharField(max_length=200)
    store_rate = models.DecimalField(
            max_length=100, 
            max_digits=3, 
            decimal_places=2,
            default=0.00,
            validators=[MinValueValidator(0.01), MaxValueValidator(5.00)])
    store_review = models.IntegerField(default=0)
    
    def __str__(self):
        return '【' + str(self.store_area) + '】 ' + str(self.store_name) + '@' + str(self.store_rate)
    
    
    
#admin
#test1010
