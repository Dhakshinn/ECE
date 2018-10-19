from django import forms
from .models import components_provided


class DateInput(forms.DateInput):
    input_type = 'date'


class ProviderFrom(forms.ModelForm):
    class Meta:
        model=components_provided
        fields = ['detail', 'quantity', 'student_name','roll_number','section', 'year', 'mobile','email_id','due_date']
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }