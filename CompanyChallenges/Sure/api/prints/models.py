from django.db import models

# Create your models here.
class Prints(models.Model):
    # Print size
    size = models.CharField(max_length=255, null=False)
    # Print cost 
    cost = models.CharField(max_length=255, null=False)
    # Print shipping cost
    shipping_cost = models.CharField(max_length=255, null=False)
    # Print total cost 
    total_cost = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.size, self.cost,self.shipping_cost, self.total_cost)