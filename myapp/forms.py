from django import forms
from .models import  Countries, Variables,  COUNTRIES, VARIABLES



class CountriesForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    country = forms.ChoiceField(choices = COUNTRIES, required = True,
                               widget = forms.Select(attrs = attrs))
    class Meta:

        model = Countries
        fields = ['country']


class VariablesForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    variable = forms.ChoiceField(choices = VARIABLES, required = True,
                               widget = forms.Select(attrs = attrs))
    class Meta:

        model = Variables
        fields = ['variable']
