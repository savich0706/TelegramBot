from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.reply_keyboards import keyboard, web_app_keyboard

# Инициализируем роутер уровня модуля
router = Router()



@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer('Чего боятся кошки больше всего?',
                         reply_markup=keyboard)
    

@router.message(Command(commands='help'))
async def process_start(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    
    
# Этот хэндлер будет срабатывать на команду "/web_app"
@router.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=web_app_keyboard
    )