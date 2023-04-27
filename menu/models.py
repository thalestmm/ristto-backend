from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    visible = models.BooleanField(default=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(max_length=100, blank=True, null=True) # TODO: Allow multiple photos
    price = models.DecimalField(max_digits=6, decimal_places=2) # TODO: Implement discounts (happy hour etc.)
    
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, null=True, blank=True)
    visible = models.BooleanField(default=True)

    ingredients = models.ManyToManyField(Ingredient) # TODO: Allow the customer to remove certain ingredients
    # TODO: implement additional items with a specific price tag

    # Item information
    lactose_free = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    # TODO: Maybe implement nutritional macros in the future

