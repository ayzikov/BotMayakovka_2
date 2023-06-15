from django.contrib import admin
from .models import Location, Image
from .forms import LocationForm, ImageForm


# регистрация моделей в админке джанго
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id',
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


    form = LocationForm


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'location_name',
                    'image_description',
                    'image')


    form = ImageForm
