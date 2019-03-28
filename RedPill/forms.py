from django import forms

class LocationSearchForm(forms.Form):
    city = forms.CharField(label="City name", max_length=100)
    postal_code = forms.IntegerField(label="Postal code")
    real_estate_type = forms.IntegerField(label="Real estate type")
    furnished = forms.BooleanField(label="Is furnished")
    owner_is_pro = forms.BooleanField(label="Is professional")
    min_price = forms.IntegerField(label="Minimum price")
    max_price = forms.IntegerField(label="Maximum price")
    min_rooms = forms.IntegerField(label="Minimum rooms")
    max_rooms = forms.IntegerField(label="Maximum rooms")
    min_square = forms.FloatField(label="Minimum square")
    max_square = forms.FloatField(label="Maximum square")