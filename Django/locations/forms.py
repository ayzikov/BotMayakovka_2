from .models import Location, Image
from django import forms
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('id',
                  'location_name',
                  'location_number',
                  'location_latitude',
                  'location_longitude',
                  'main_text',
                  'detailed_description',
                  'audio_guide_text',
                  'audio_guide',
                  'additionally',
                  'additionally_button')

        widgets = {
            'location_name': forms.Textarea(attrs={'rows': 2, 'cols': 45}),
            'location_number': forms.NumberInput(),
            'location_latitude': forms.NumberInput(),
            'location_longitude': forms.NumberInput(),
            'main_text': forms.Textarea(attrs={'rows': 6, 'cols': 60}),
            'audio_guide_text': forms.Textarea(attrs={'rows': 2, 'cols': 45}),
            'additionally_button': forms.TextInput()

        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('id',
                  'name',
                  'location_name',
                  'image_description',
                  'image')

        widgets = {
            'name': forms.TextInput(),
            'image_description': forms.Textarea(attrs={'rows': 6, 'cols': 60})
        }