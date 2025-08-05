from django import forms
from .models import StudentModel

class StdReader(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name', 'rollno', 'cource']