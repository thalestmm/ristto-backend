from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(Ingredient)
admin.site.register(MenuItem)