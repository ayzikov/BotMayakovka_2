from django.db import models



# модель для локации
class Location(models.Model):
    location_name = models.TextField(verbose_name='Название локации')
    location_number = models.IntegerField(verbose_name='Номер локации')
    next_location_latitude = models.FloatField(verbose_name='Широта следующей локации')
    next_location_longitude = models.FloatField(verbose_name='Долгота следующей локации')
    main_text = models.TextField(verbose_name='Главное описание локации')
    detailed_description = models.TextField(verbose_name='Подробное описание локации')

    audio_guide_text = models.TextField(verbose_name='Описание к голосовому',
                                        blank=True)

    audio_guide = models.FileField(verbose_name='Голосовое сообщение',
                                   upload_to='audio/')

    additionally = models.TextField(verbose_name='Дополнительный текст локации')
    additionally_button = models.TextField(verbose_name='Название дополнительной кнопки')

    next_button_text = models.TextField(verbose_name='Текст для кнопки "Дальше"',
                                        default='')



    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


# модель для изображения
class Image(models.Model):
    BUTTONS = [
        ('Я на месте', 'Я на месте'),
        ('Подробное описание', 'Подробное описание'),
        ('Дополнительно', 'Дополнительно')
    ]

    name = models.CharField(verbose_name='Название кнопки',
                            max_length=99,
                            choices=BUTTONS,
                            default='Я на месте')

    image_description = models.TextField(verbose_name='Описание изображения',
                                         blank=True)

    location_name = models.ForeignKey(to=Location, on_delete=models.CASCADE, verbose_name='Локация к которой привязано изображение')

    location_number = models.IntegerField(verbose_name='Номер локации',
                                          default=0)

    image = models.ImageField(verbose_name='Изображение для локации',
                              upload_to='images/',
                              blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class User(models.Model):
    user_tg_id = models.IntegerField(verbose_name='id пользователя в телеграме')
    full_name = models.TextField(verbose_name='Имя пользователя при наличии', default='')
    username = models.TextField(verbose_name='Юзернейм пользователя при наличии', default='')
    reg_time = models.DateTimeField(verbose_name='Дата регистрации пользователя')
    last_time = models.DateTimeField(verbose_name='Дата последнего действия пользователя')
    counter_locations = models.IntegerField(verbose_name='Количество пройденных локаций', default=0)

class Action(models.Model):
    msg_name = models.TextField(verbose_name='Название выполненной команды')
    click_time = models.DateTimeField(verbose_name='время и дата выполненной команды')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь который совершил действие')