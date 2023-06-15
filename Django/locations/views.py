import json

from .models import Location
from .serializers import LocationSerializer

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

        location_info = Location.objects.get(location_number=location_number)

        return Response(LocationSerializer(location_info).data)