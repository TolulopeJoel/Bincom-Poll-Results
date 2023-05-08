from django import forms
from .models import Lga

class LGAForm(forms.Form):
    lga = forms.ModelChoiceField(queryset=Lga.objects.all())

    def __init__(self, *args, **kwargs):
        super(LGAForm, self).__init__(*args, **kwargs)

        for value in self.visible_fields():
            value.field.widget.attrs['class'] = 'form-control w-100'

