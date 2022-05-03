from django import forms

from crud.models import StudentClass


class CreateStudentClassForm(forms.ModelForm):
    class Meta:
        model  = StudentClass
        fields = [
            'class_id',
            'grade',
        ]