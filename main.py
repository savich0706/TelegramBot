import asyncio

from aiogram import Bot, Dispatcher
from configuration.config import Config, load_config
from handlers import user_handlers, other_hendlers


async def main():
    # Загружаем конфиг в переменную
    config: Config = load_config()
    
    # инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    
    # подключаем роутеры к диспетчеру
    dp.include_routers(user_handlers.router, other_hendlers.router)
    
    # Пропускаем накопившиеся апдейты и запускаем полинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

