from .models import Location, Image
from django import forms


# формы для отображения полей в админ панели
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('id',
                  'location_name',
                  'location_number',
                  'next_location_latitude',
                  'next_location_longitude',
                  'main_text',
                  'detailed_description',
                  'audio_guide_text',
                  'audio_guide',
                  'additionally',
                  'additionally_button',
                  'next_button_text')

        widgets = {
            'location_name': forms.Textarea(attrs={'rows': 2, 'cols': 45}),
            'location_number': forms.NumberInput(),
            'next_location_latitude': forms.NumberInput(),
            'next_location_longitude': forms.NumberInput(),
            'main_text': forms.Textarea(attrs={'rows': 6, 'cols': 60}),
            'audio_guide_text': forms.Textarea(attrs={'rows': 2, 'cols': 45}),
            'additionally_button': forms.TextInput(),
            'next_button_text': forms.Textarea(attrs={'rows': 2, 'cols': 45})

        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('id',
                  'name',
                  'location_name',
                  'location_number',
                  'image_description',
                  'image')

        widgets = {
            'image_description': forms.Textarea(attrs={'rows': 6, 'cols': 60})
        }