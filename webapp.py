from flask import Flask, render_template, send_from_directory, request, jsonify
import os
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание Flask приложения
app = Flask(__name__)

# Конфигурация
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-12345')
app.config['DEBUG'] = os.environ.get('DEBUG', 'True').lower() == 'true'

# ============================================
# ГЛАВНЫЕ СТРАНИЦЫ
# ============================================

@app.route('/')
def index():
    """Главная страница - редирект на games"""
    logger.info(f"Запрос главной страницы от {request.remote_addr}")
    return render_template('games.html')

@app.route('/games')
def games():
    """Страница со списком всех игр"""
    logger.info(f"Запрос списка игр от {request.remote_addr}")
    
    # Если есть данные пользователя из Telegram
    user_data = None
    if request.args.get('user'):
        user_data = request.args.get('user')
    
    return render_template('games.html', user=user_data)

@app.route('/health')
def health():
    """Проверка здоровья сервера"""
    return jsonify({
        'status': 'ok',
        'time': datetime.now().isoformat(),
        'games_count': 20
    })

# ============================================
# МАРШРУТЫ ДЛЯ ВСЕХ 20 ИГР
# ============================================

# 🔫 Экшн и спорт (5 игр)
@app.route('/play/darts')
def play_darts():
    """Игра 1: Дартс"""
    logger.info("Запуск игры: Дартс")
    return render_template('games/darts.html')

@app.route('/play/penalty')
def play_penalty():
    """Игра 2: Пенальти"""
    logger.info("Запуск игры: Пенальти")
    return render_template('games/penalty.html')

@app.route('/play/punch')
def play_punch():
    """Игра 3: Удар силой"""
    logger.info("Запуск игры: Удар силой")
    return render_template('games/punch.html')

@app.route('/play/duel')
def play_duel():
    """Игра 4: Дуэль"""
    logger.info("Запуск игры: Дуэль")
    return render_template('games/duel.html')

@app.route('/play/robot_battle')
def play_robot_battle():
    """Игра 5: Битва роботов"""
    logger.info("Запуск игры: Битва роботов")
    return render_template('games/robot_battle.html')

# 🧩 Головоломки (5 игр)
@app.route('/play/puzzle')
def play_puzzle():
    """Игра 6: Пазл"""
    logger.info("Запуск игры: Пазл")
    return render_template('games/puzzle.html')

@app.route('/play/chemistry')
def play_chemistry():
    """Игра 7: Химия"""
    logger.info("Запуск игры: Химия")
    return render_template('games/chemistry.html')

@app.route('/play/snake')
def play_snake():
    """Игра 8: Змейка"""
    logger.info("Запуск игры: Змейка")
    return render_template('games/snake.html')

@app.route('/play/quiz')
def play_quiz():
    """Игра 9: Викторина"""
    logger.info("Запуск игры: Викторина")
    return render_template('games/quiz.html')

@app.route('/play/archery')
def play_archery():
    """Игра 10: Лук и стрелы"""
    logger.info("Запуск игры: Лук и стрелы")
    return render_template('games/archery.html')

# 🎰 Азартные игры (4 игры)
@app.route('/play/dice')
def play_dice():
    """Игра 11: Кости"""
    logger.info("Запуск игры: Кости")
    return render_template('games/dice.html')

@app.route('/play/blackjack')
def play_blackjack():
    """Игра 12: 21 очко"""
    logger.info("Запуск игры: 21 очко")
    return render_template('games/blackjack.html')

@app.route('/play/slots')
def play_slots():
    """Игра 13: Слот-машина"""
    logger.info("Запуск игры: Слот-машина")
    return render_template('games/slots.html')

@app.route('/play/fishing')
def play_fishing():
    """Игра 14: Рыбалка"""
    logger.info("Запуск игры: Рыбалка")
    return render_template('games/fishing.html')

# 🏁 Гонки (2 игры)
@app.route('/play/space_racer')
def play_space_racer():
    """Игра 15: Космо-рейсер"""
    logger.info("Запуск игры: Космо-рейсер")
    return render_template('games/space_racer.html')

@app.route('/play/retro_racer')
def play_retro_racer():
    """Игра 16: Ретро-гонки"""
    logger.info("Запуск игры: Ретро-гонки")
    return render_template('games/retro_racer.html')

# 🎨 Творческие (2 игры)
@app.route('/play/drawing')
def play_drawing():
    """Игра 17: Рисовалка"""
    logger.info("Запуск игры: Рисовалка")
    return render_template('games/drawing.html')

@app.route('/play/rhythm')
def play_rhythm():
    """Игра 18: Ритм-игра"""
    logger.info("Запуск игры: Ритм-игра")
    return render_template('games/rhythm.html')

# 👑 Стратегии (2 игры)
@app.route('/play/kingdom')
def play_kingdom():
    """Игра 19: Королевство"""
    logger.info("Запуск игры: Королевство")
    return render_template('games/kingdom.html')

@app.route('/play/arcade')
def play_arcade():
    """Игра 20: Ретро-аркада"""
    logger.info("Запуск игры: Ретро-аркада")
    return render_template('games/arcade.html')

# ============================================
# API ДЛЯ СТАТИСТИКИ (опционально)
# ============================================

@app.route('/api/games/list')
def api_games_list():
    """API: список всех игр"""
    games = [
        {"id": 1, "name": "Дартс", "emoji": "🎯", "url": "/play/darts"},
        {"id": 2, "name": "Пенальти", "emoji": "⚽", "url": "/play/penalty"},
        {"id": 3, "name": "Удар силой", "emoji": "🥊", "url": "/play/punch"},
        {"id": 4, "name": "Дуэль", "emoji": "🤠", "url": "/play/duel"},
        {"id": 5, "name": "Битва роботов", "emoji": "🤖", "url": "/play/robot_battle"},
        {"id": 6, "name": "Пазл", "emoji": "🧩", "url": "/play/puzzle"},
        {"id": 7, "name": "Химия", "emoji": "🧪", "url": "/play/chemistry"},
        {"id": 8, "name": "Змейка", "emoji": "🐍", "url": "/play/snake"},
        {"id": 9, "name": "Викторина", "emoji": "🧠", "url": "/play/quiz"},
        {"id": 10, "name": "Лук и стрелы", "emoji": "🏹", "url": "/play/archery"},
        {"id": 11, "name": "Кости", "emoji": "🎲", "url": "/play/dice"},
        {"id": 12, "name": "21 очко", "emoji": "🃏", "url": "/play/blackjack"},
        {"id": 13, "name": "Слот-машина", "emoji": "🎰", "url": "/play/slots"},
        {"id": 14, "name": "Рыбалка", "emoji": "🎣", "url": "/play/fishing"},
        {"id": 15, "name": "Космо-рейсер", "emoji": "🚀", "url": "/play/space_racer"},
        {"id": 16, "name": "Ретро-гонки", "emoji": "🏁", "url": "/play/retro_racer"},
        {"id": 17, "name": "Рисовалка", "emoji": "🎨", "url": "/play/drawing"},
        {"id": 18, "name": "Ритм-игра", "emoji": "🎵", "url": "/play/rhythm"},
        {"id": 19, "name": "Королевство", "emoji": "👑", "url": "/play/kingdom"},
        {"id": 20, "name": "Ретро-аркада", "emoji": "🎮", "url": "/play/arcade"}
    ]
    return jsonify(games)

@app.route('/api/stats/<game_name>')
def api_game_stats(game_name):
    """API: статистика по конкретной игре"""
    return jsonify({
        'game': game_name,
        'plays': 0,
        'avg_score': 0
    })

# ============================================
# СТАТИЧЕСКИЕ ФАЙЛЫ
# ============================================

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Раздача статических файлов (CSS, JS, изображения)"""
    return send_from_directory('static', filename)

# ============================================
# ОБРАБОТКА ОШИБОК
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Страница 404"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Страница 500"""
    logger.error(f"Server error: {error}")
    return render_template('500.html'), 500

# ============================================
# ЗАПУСК ПРИЛОЖЕНИЯ
# ============================================

if __name__ == '__main__':
    # Получаем порт из переменных окружения (для Railway/Render)
    port = int(os.environ.get('PORT', 5000))
    
    # Режим отладки
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'
    
    # Запускаем сервер
    logger.info(f"Запуск Flask сервера на порту {port}")
    logger.info(f"Режим отладки: {debug}")
    logger.info(f"Доступные игры: 20")
    
    app.run(
        host='0.0.0.0',  # Слушаем все интерфейсы
        port=port,
        debug=debug
    )
