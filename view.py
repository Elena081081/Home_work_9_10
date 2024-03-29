from aiogram import types
from create_bot import bot

async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет! '
    f'Сегодня будем делить конфеты.\n'
    'На столе лежит опредленное количестов конфет (их количество можно изменить командой "/set").\n'
    'За один раз можно взять не больше определенного количества конфет (количество можно изменить командой "/take").\n'
    'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
    'Можно задать уровень сложности командой "/level".\n' 
    'Уровень 1 - "умный бот", его очень сложно обыграть.\n'
    'Уровень 2 - "глупый бот", на нем можно потренироваться.' )
