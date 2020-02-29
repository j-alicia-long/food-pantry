from django import forms

class FoodForm(forms.Form):
    food_item = forms.CharField(label='food for fridge', max_length = 20)
    expiration_date = forms.DateTimeField('expiration date')
    