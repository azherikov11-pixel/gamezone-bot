import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Читаем токен и URL из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')  # ← читает из .env
WEBAPP_URL = os.getenv('WEBAPP_URL')  # ← читает из .env

# Проверка, что токен загрузился
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Проверь .env файл")

if not WEBAPP_URL:
    raise ValueError("❌ WEBAPP_URL не найден! Проверь .env файл")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    
    web_app_button = types.InlineKeyboardButton(
        text="🎮 Играть в мини-игры",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    keyboard.add(web_app_button)
    
    await message.answer(
        "🎮 *Добро пожаловать в GameZone\\!*\n\n"
        "Нажми на кнопку ниже, чтобы открыть портал с 20 мини\-играми\\.",
        reply_markup=keyboard,
        parse_mode="MarkdownV2"
    )

if __name__ == '__main__':
    print(f"✅ Бот запущен с токеном: {BOT_TOKEN[:10]}...")
    print(f"🌐 WebApp URL: {WEBAPP_URL}")
    executor.start_polling(dp, skip_updates=True)
