
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             
from aiogram.filters.command import Command   
from transliterate import translit


TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)                        
dp = Dispatcher()                             
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    
@dp.message()
async def translate_name(message: Message):
    user_name = message.text.strip()
    if user_name:
        try:
            transliterated_name = translit(user_name, reversed=True) 
            response_text = f'Ваше имя на латинице: {transliterated_name}'
        except Exception as e:
            response_text = f'Произошла ошибка при конвертации имени: {str(e)}'
    else:
        response_text = 'Пожалуйста, отправьте ваше ФИО.'

    await message.answer(response_text)

if __name__ == '__main__':
    dp.run_polling(bot)