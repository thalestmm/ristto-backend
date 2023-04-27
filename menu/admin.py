from django.contrib import admin
from .models import *

# Custom Admin Panel actions
@admin.action(description="Make itens visible on the menu")
def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)

@admin.action(description="Make itens invisible on the menu")
def make_invisible(modeladmin, request, queryset):
    queryset.update(visible=False)


# Model Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "visible", "gluten_free", "lactose_free", "vegan"]
    ordering = ["-category", "-visible", "name"]
    actions = [make_visible, make_invisible]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "visible"]
    ordering = ["name", "visible"]
    actions = [make_visible, make_invisible]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient)
admin.site.register(Item, ItemAdmin)