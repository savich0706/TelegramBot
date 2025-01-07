from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


TOKEN = '7967376653:AAFNc3mZmNM7IXYm2-4S6dNjuRtP4q_LsWs'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет, я Бот, напиши что нибудь!')
    

@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Вы выбрали помощь')


@dp.message()
async def all_message(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except:
        await message.reply(text='Данный тип апдейтов не поддерживается')
    
    
    
@dp.message(F.photo)
async def process_photo_message(message: Message):
    await message.reply_photo(message.photo[-1].file_id, caption='Это Ваше фото')
  

if __name__ == '__main__':
    dp.run_polling(bot)

