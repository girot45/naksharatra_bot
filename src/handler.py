import os
import time
from datetime import date
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from astropy.coordinates import EarthLocation

from naksharatra.nakshatra_calculations import \
    calc_nakshatra_tithi
from states import UserData
from settings import bot_settings

naksha_router = Router()


@naksha_router.callback_query(F.data == "start_nakshatra")
async def start_nakshatra(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(bot_settings.enter_country_message)
    await state.set_state(UserData.country)


@naksha_router.message(
    UserData.country,
)
async def get_country(message: types.Message, state:FSMContext):
    country = bot_settings.translator.translate(message.text, dest="en").text
    await state.update_data(country=country)
    await message.answer(bot_settings.enter_city_message)
    await state.set_state(UserData.city)


@naksha_router.message(
    UserData.city,
)
async def get_country(message: types.Message, state:FSMContext):
    city = bot_settings.translator.translate(message.text, dest="en").text
    data = await state.get_data()
    print(f"{data['country'], {city}}")
    observing_location = EarthLocation.of_address(f"{data['country'], {city}}")
    print(observing_location)
    try:
        print(observing_location.lon.value, observing_location.lat.value)
    except:
        await message.answer(bot_settings.location_error_message)
        await state.clear()
        return
    await state.update_data(city=city)
    await message.answer(bot_settings.enter_date_message)
    await state.set_state(UserData.date_)


@naksha_router.message(
    UserData.date_,
    F.text.regexp(
        "[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])")
)
async def get_date(message: types, state: FSMContext):
    try:
        if date.fromisoformat(message.text.lower()):
            pass
        await state.update_data(date_=message.text.lower())

        await message.answer(bot_settings.enter_time_message)
        await state.set_state(UserData.time_)
    except ValueError:
        await message.answer(bot_settings.enter_date_message_error)
        return

@naksha_router.message(UserData.date_)
async def date_incorrectly(message: types.Message):
    await message.answer(bot_settings.enter_date_message)


@naksha_router.message(
    UserData.time_,
    F.text.regexp("^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
)
async def get_time(message: types.Message, state: FSMContext):
    try:
        user_data = await state.get_data()
        if time.strptime(message.text, "%H:%M"):
            pass
        time_ = message.text + ":00"
        date_time = user_data["date_"] + " " + time_
        print(user_data["city"] + ", " + user_data["country"],
            date_time)
        calc_nakshatra_tithi(
            location=user_data["city"] + ", " + user_data["country"],
            time=date_time,
        )
        await message.reply_photo(
            photo=types.FSInputFile(path="res_img/res.png")
        )
        os.remove("res_img/res.png")

    except ValueError:
        await message.answer(bot_settings.enter_time_message_error)
        return


@naksha_router.message(UserData.time_)
async def time_incorrect(message: types.Message):
    await message.answer(bot_settings.enter_time_message)
