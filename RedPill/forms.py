from django import forms

class LocationSearchForm(forms.Form):
    city = forms.CharField(label="City name", max_length=100, initial="City name")
    postal_code = forms.CharField(label="Postal code", max_length=5, initial="00000")
    real_estate_type = forms.IntegerField(label="Real estate type", initial=1, min_value=1, max_value=4)
    furnished = forms.BooleanField(label="Is furnished", required=False)
    owner_is_pro = forms.BooleanField(label="Is from professional", required=False)
    min_price = forms.IntegerField(label="Minimum price", initial=0, min_value=0)
    max_price = forms.IntegerField(label="Maximum price", initial=1000, min_value=0)
    min_rooms = forms.IntegerField(label="Minimum rooms", initial=0, min_value=0)
    max_rooms = forms.IntegerField(label="Maximum rooms", initial=3, min_value=0)
    min_square = forms.FloatField(label="Minimum square", initial=0, min_value=0)
    max_square = forms.FloatField(label="Maximum square", initial=100, min_value=0)