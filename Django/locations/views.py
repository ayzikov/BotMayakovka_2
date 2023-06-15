import json

from .models import Location, Image
from .serializers import LocationSerializer, ImageSerializer

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


def get_dict_from_json(val, request):
    '''Функция преобразования json объекта в dict'''

    json_data = request.body.decode('utf-8')  # преобразование байтовой строки в строку
    data = json.loads(json_data)  # преобразование JSON-строки в словарь Python
    return data.get(val)  # получение значения по ключу 'val'


class LocationView(APIView):
    def get(self, request: Request):

        # преобразование входящих данных
        location_number = get_dict_from_json(val='location_number', request=request)

        # получение объекта локации из БД по ее номеру
        location_info = Location.objects.get(location_number=location_number)

        # отправка JSON
        return Response(LocationSerializer(location_info).data)


class ImagesView(APIView):
    def get(self, request: Request):

        # преобразование входящих данных
        location_number = get_dict_from_json(val='location_number', request=request)

        # получение объектов изображений из БД по номеру локации
        images_info = Image.objects.filter(location_number=location_number)

        # отправка JSON
        try:
            return Response(ImageSerializer(images_info, many=True).data)
        except:
            return Response(ImageSerializer(images_info).data)