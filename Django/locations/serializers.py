from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    location_name = serializers.CharField(max_length=9999)
    location_number = serializers.IntegerField()
    next_location_latitude = serializers.FloatField()
    next_location_longitude = serializers.FloatField()
    main_text = serializers.CharField(max_length=9999)
    detailed_description = serializers.CharField(max_length=9999)
    audio_guide_text = serializers.CharField(max_length=9999)
    audio_guide = serializers.FileField()
    additionally = serializers.CharField(max_length=9999)
    additionally_button = serializers.CharField(max_length=9999)
    next_button_text = serializers.CharField(max_length=9999)


class ImageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=999)
    image_description = serializers.CharField(max_length=999)
    location_name = serializers.CharField(max_length=999)
    location_number = serializers.IntegerField()
    image = serializers.FileField(max_length=999)