import random
from config import bot,dp
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from database.db import sql_command_random
from parseryr.Arkasha import parser


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Who's your president?"
    answer = [
        "Michael Jordan",
        "Barack Obama",
        "Jooomart Tokaev",
        "Jeenbekov"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation="Bbal is life",
        open_period=60,
        reply_markup=markup
    )


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("Надо ответить на сообщение!")


async def show_random_user(message: types.Message):
    await sql_command_random(message)

async def films_parser(message: types.Message):
    films = parser()
    for fily in films:
        await bot.send_message(
            message.from_user.id,
            f"{fily['year']}\n"
            f"#{fily['gengre']}\n\n"
            f"{fily['link']}"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands="quiz")
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(show_random_user, commands=['get'])
    dp.register_message_handler(films_parser, commands=["films"])


