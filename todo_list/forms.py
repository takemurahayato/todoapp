from django import forms
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]

class ChoiceForm(forms.Form):
    choice = forms.fields.ChoiceField(
        choices=(
            ('1', '高'),
            ('2', '中'),
            ('3', '低')
        ),
        required=True,
        widget=forms.widgets.Select
    )
