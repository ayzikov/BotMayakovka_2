import json
from datetime import datetime, time, timedelta

from .models import Location, Image, User, Action
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


def get_current_datetime():
    '''
    Функция расчитывает конец и начало текущих дня и недели
    :return: 4 datetime объекта
    '''

    current_day = datetime.now() + timedelta(hours=3)
    start_day = datetime.combine(current_day.date(), time.min)
    end_day = datetime.combine(current_day.date(), time.max)

    current_week_day = datetime.now().weekday()
    start_week = datetime.now() + timedelta(hours=3) - timedelta(days=current_week_day,
                                            hours=(datetime.now() + timedelta(hours=3)).hour,
                                            minutes=(datetime.now() + timedelta(hours=3)).minute,
                                            seconds=(datetime.now() + timedelta(hours=3)).second)
    end_week = start_week + timedelta(days=6,
                                      hours=23,
                                      minutes=59,
                                      seconds=59)

    return start_day, end_day, start_week, end_week


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


class UserAddView(APIView):
    def post(self, request: Request):
        '''
        функция проверяет наличие пользователи и добавляет его в БД, если его нет
        '''

        # получаем из данные в том числе и из запроса
        user_tg_id = get_dict_from_json(val='user_tg_id', request=request)
        full_name = get_dict_from_json(val='full_name', request=request)
        username = get_dict_from_json(val='username', request=request)
        reg_time = last_time = datetime.now() + timedelta(hours=3)

        # проверяем наличие пользователя в БД - если его там нет записываем данные
        try:
            User.objects.get(user_tg_id=user_tg_id)
        except:
            User.objects.create(user_tg_id=user_tg_id,
                                full_name=full_name,
                                username=username,
                                reg_time=reg_time,
                                last_time=last_time)

        return Response('Пользователь добавлен')


class ActionView(APIView):
    def post(self, request: Request):
        '''
        функция добавляет действие в БД
        '''

        # получаем из данные в том числе и из запроса
        msg_name = get_dict_from_json(val='msg_name', request=request)
        click_time = datetime.now() + timedelta(hours=3)
        location_number = get_dict_from_json(val='location_number', request=request)
        user_tg_id = get_dict_from_json(val='user_tg_id', request=request)
        user = User.objects.filter(user_tg_id=user_tg_id)

        # добавляем действие в БД
        Action.objects.create(msg_name=msg_name,
                              click_time=click_time,
                              user=user[0])

        # обновляем время последнего входа пользователя
        user.update(last_time=datetime.now() + timedelta(hours=3))

        # если это команда "Я на месте" - обновляем счетчик локаций пройденных пользователем
        if msg_name == 'Я на месте':
            user.update(counter_locations=location_number)

        return Response('Действие создано')