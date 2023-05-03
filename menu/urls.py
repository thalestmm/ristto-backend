from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>', views.get_items_by_category, name='category_menu'),
]
