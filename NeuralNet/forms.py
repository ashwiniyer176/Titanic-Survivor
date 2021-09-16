from django import forms


class InputForm(forms.Form):
    PClass = forms.IntegerField(label='Passenger Class')
    gender = forms.ChoiceField(choices=[(1, 'Male'), (0, 'Female')])
    age = forms.IntegerField(label="Age")
    fare = forms.FloatField(label="Ticket Fare")
    family = forms.IntegerField(label="Family Members on Board")
