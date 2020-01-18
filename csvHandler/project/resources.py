from import_export import resources
from .models import Person, Restaurant

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant
