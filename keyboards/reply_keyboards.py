from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


kb_builder = ReplyKeyboardBuilder()

buttons: list[KeyboardButton] = [
    KeyboardButton(text='phone number', request_contact=True),
    KeyboardButton(text='geolocation', request_location=True),
    KeyboardButton(text='create victorine', request_poll=KeyboardButtonPollType())
]

kb_builder.row(*buttons, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

# Создаем кнопку
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://youtube.com/"))


# Создаем объект клавиатуры
web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True)