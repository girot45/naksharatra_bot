
import asyncio

from handler import naksha_router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from googletrans import Translator

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from naksharatra.nakshatra_calculations import \
    calc_nakshatra_tithi
from settings import bot_settings

location = "Moscow, Russia"
date_str = "2002-11-11 00:35:00"

calc_nakshatra_tithi(location=location, time=date_str)

translator = Translator()
bot = Bot(token=bot_settings.token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=bot_settings.button_text,
        callback_data=bot_settings.callback_data)
    )
    await message.answer(
        bot_settings.start_message,
        reply_markup=builder.as_markup()
    )


dp.include_router(naksha_router)

# @dp.message()
# async def get_nakha(message: types.Message):
#     items = message.text.split(",")
#     res = []
#     for i in items:
#         res.append(translator.translate(i, dest='en').text)
#     location = ", ".join(res[:2])
#
#     date_ = " ".join(res[2:4]) + ":00"
#     calc_nakshatra_tithi(location, date_, fs=12, filename="src/res_img/res.png")
#     # Отправляем изображение
#     await message.reply_photo(
#         photo=types.FSInputFile(path="src/res_img/res.png")
#     )
#
#     # Удаляем изображение после отправки
#     os.remove("src/res_img/res.png")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())