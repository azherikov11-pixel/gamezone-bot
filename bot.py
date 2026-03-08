import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import os

# Токен твоего бота от @BotFather
BOT_TOKEN = "7902364192:AAEF20GyevxN-ao_jPj-dx7y5Cs73jD-hFM"
# Ссылка на твой сайт (об этом позже)
# Если запускаешь локально, используй ссылку из ngrok или локальный сервер с https
WEBAPP_URL = "https://твой-сайт.ру/games" # Сюда впишем адрес позже

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Создаем клавиатуру с WebApp кнопкой
    keyboard = types.InlineKeyboardMarkup()
    
    # Главная кнопка, которая откроет сайт с играми
    web_app_button = types.InlineKeyboardButton(
        text="🎮 Играть в мини-игры",
        web_app=types.WebAppInfo(url=WEBAPP_URL) # <-- Вот тут магия!
    )
    keyboard.add(web_app_button)
    
    await message.answer(
        "🎮 *Добро пожаловать в игровой зал\!*\n\n"
        "Нажми на кнопку ниже, чтобы открыть портал с 20 увлекательными мини\-играми\.\n"
        "Игры запускаются прямо в Telegram\!",
        reply_markup=keyboard,
        parse_mode="MarkdownV2"
    )

# Запуск бота (polling)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
