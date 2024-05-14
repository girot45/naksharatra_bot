import os
from dotenv import load_dotenv
from googletrans import Translator

load_dotenv()

class Settings:
    translator = Translator()
    token: str = os.environ.get('TOKEN')
    start_message: str = 'Что бы получить карту нажмите на кнопку'
    button_text: str = 'Рассчитать карту'
    callback_data: str = 'start_nakshatra'
    enter_city_message: str = 'Введите город, в котором вы родились'
    enter_country_message: str = 'Введите страну, в которой вы родились'
    location_error_message: str = ('Не можем найти такую локацию. '
                                   'Введите сначала')
    enter_date_message: str = 'Введите дату в формате год-месяц-день. \nПример: 2024-12-31'
    enter_date_message_error: str = 'Такой даты не существует. Попробуйте еще раз'
    enter_time_message: str = 'Введите время в формате часы:минуты. \nПример: 23:59'
    enter_time_message_error: str = 'Такого времени не существует. Попробуйте еще раз'
