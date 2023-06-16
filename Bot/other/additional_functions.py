async def parsing_images(images_info: list, button_name: str):
    '''
    Функция парсит список со всеми изображениями локации
    :param images_info: список со словарями инофрмации о изображениях
    :param button_name: имя кнопки к которой привязаны изображения
    :return: список состоящий из кортежей, (путь к изображению, описание изображения, если есть)
    '''

    result = []

    # берем по одному словарю
    for dt in images_info:
        if dt['name'] == button_name:
            result.append((dt['image'], dt['image_description']))

    return result