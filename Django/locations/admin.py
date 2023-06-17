from django.contrib import admin
from .models import Location, Image
from .forms import LocationForm, ImageForm


# регистрация моделей в админке джанго
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id',
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


    form = LocationForm


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'location_name',
                    'location_number',
                    'image_description',
                    'image')


    form = ImageForm
