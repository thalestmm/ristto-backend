from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_default_user():
    """
    Returns the dev user as a default for creating a new Model instace
    """
    return User.objects.get(username='dev')

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)

    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField(max_length=200)
    owner_telephone = models.CharField(max_length=20)

    user_admin = models.ForeignKey(User, default=get_default_user, on_delete=models.SET_DEFAULT)

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    visible = models.BooleanField(default=True)
    section_name = models.CharField(max_length=50, null=True, blank=True)

    menu = models.ForeignKey(Menu, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.section_name:
            self.section_name = self.name.lower().replace(" ", "-")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["name", "visible"]

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(max_length=100, blank=True, null=True, upload_to='menu') 
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    # TODO: Implement discounts (happy hour etc.) -> This could be another category (and be limited to a certain time of day)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    visible = models.BooleanField(default=True)

    # TODO: Allow the customer to remove certain ingredients -> add an observations field
    # ? For plates with meat, allow them to set the desired point

    # Item information
    lactose_free = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    # ? Maybe implement nutritional macros in the future

    # Use this speacilly for wines, but any plate might have this
    origin_country_code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        # Save the uploaded photo with a standardized filename
        if self.photo:
            photo_extension = "." + self.photo.name.split(".")[1]
            self.photo.name = str(self.id) + photo_extension
            # FIXME: Delete the unused uploaded photos from the media root when the models is saved -> Maybe do this in the admin panel
        super().save(*args, **kwargs)


    class Meta:
        ordering = ["-category", "name", "visible"]