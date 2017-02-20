from django import forms

class DivisionForm (forms.Form):
    dividend = forms.FloatField(label='Dividend')
    divisor = forms.FloatField(label='Divisor')
