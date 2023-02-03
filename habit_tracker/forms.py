from .models import ModelHabit
from django.forms import ModelForm, DateInput
from django import forms

class FormHabit(ModelForm):
    class Meta:
        model = ModelHabit
        fields = ("label", "periodicity", "begin_date", "end_date")
        widgets = {
            "label": forms.TextInput(attrs={"class": "form-control"}),
            "periodicty": forms.Select(attrs={"class": "form-control"}),
            "begin_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": "form-control"})
        }