from django import forms

from .models import AnnouncedPollingUnitResult, Lga, PollingUnit


class LGAForm(forms.Form):
    lga = forms.ModelChoiceField(queryset=Lga.objects.all())

    def __init__(self, *args, **kwargs):
        super(LGAForm, self).__init__(*args, **kwargs)

        for value in self.visible_fields():
            value.field.widget.attrs['class'] = 'form-control w-100'


class PollingUnitResultForm(forms.ModelForm):
    polling_unit = forms.ModelChoiceField(queryset=PollingUnit.objects.all())

    class Meta:
        model = AnnouncedPollingUnitResult
        fields = ['polling_unit', 'party', 'party_score']
        

    def __init__(self, *args, **kwargs):
        super(PollingUnitResultForm, self).__init__(*args, **kwargs)

        for value in self.visible_fields():
            value.field.widget.attrs['class'] = 'form-control w-100'
