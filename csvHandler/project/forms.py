from django.forms import ModelForm, TextInput
from .models import City, Restaurant, Feed_Message


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}

class RestaurantForm(ModelForm):
    class Meta:
        model = Feed_Message
        fields = ['week','day']
        widgets = {
        'week' : TextInput(attrs={'class' : 'input', 'placeholder' : 'week'}),
        'day' : TextInput(attrs={'class' : 'input', 'placeholder' : 'day'}),
        }
