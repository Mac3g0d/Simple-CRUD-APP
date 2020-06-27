from django import forms
from .models import CRUD


class CRUDForm(forms.ModelForm):
    class Meta:
        model = CRUD
        fields = "__all__"
