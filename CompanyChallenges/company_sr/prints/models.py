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
        return "{} - {} - {} - {}".format(self.size, self.cost,self.shipping_cost, self.total_cost)

# Create your models here.
class Order(models.Model):

    first_name = models.CharField(max_length=255, null=False)

    last_name = models.CharField(max_length=255, null=False)
    
    email = models.CharField(max_length=255, null=False)
    
    phone_number = models.CharField(max_length=255, null=False)
    
    address_one = models.CharField(max_length=255, null=False)

    address_two = models.CharField(max_length=255, null=False)

    city = models.CharField(max_length=255, null=False)
    
    state = models.CharField(max_length=255, null=False)
    
    postal_code = models.CharField(max_length=255, null=False)
    
    country = models.CharField(max_length=255, null=False)

    photo_name = models.CharField(max_length=255, null=False)

    photo_size = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.first_name, 
                                self.last_name, self.email, self.phone_number, self.address_one,
                                self.address_two, self.city, self.state, self.postal_code, self.country,
                                self.photo_name, self.photo_size)

class Photo(models.Model):

    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return "{}".format(self.name)
