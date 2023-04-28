from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["name", "visible"]

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(max_length=100, blank=True, null=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    # TODO: Implement discounts (happy hour etc.) -> This could be another category (and be limited to a certain time of day)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    visible = models.BooleanField(default=True)

    # TODO: Allow the customer to remove certain ingredients (add an observations field)
    # TODO: For plates with meat, allow them to set the desired point

    # Item information
    lactose_free = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    # TODO: Maybe implement nutritional macros in the future

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-category", "name", "visible"]