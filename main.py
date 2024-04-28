import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from model import classify_inquiry
from dotenv import dotenv_values
import json
from heandlers import router

config = dotenv_values("config/config.env")
token = config['TOKEN']

bot = Bot(token=token)
dp = Dispatcher()

with open ("answer_class_dict.json","r",encoding="utf-8") as file:
    output = json.load(file)

class Quest(StatesGroup):
    q = State()


@router.message(F.text == 'У меня вопрос!')
async def quest(message: Message, state: FSMContext):
    text = message.text
    print(f'[LOG] --> {message.from_user.username} --> {text}')
    await state.set_state(Quest.q)
    await message.reply(f'Слушаю {message.from_user.username}')


@router.message(Quest.q)
async def take_quest(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(q=message.text)
    quest = await state.get_data()
    answ = output[str(classify_inquiry(quest["q"]))]
    print(answ)
    if quest["q"] == 'оператора сюда':
        await bot.send_message(chat_id=1969348342, text=f'Студент @{message.from_user.username} спрашивает:\n"{quest["q"]}"')
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(name)s - %(message)s - (%(filename)s).%(funcName)s: %(lineno)d'
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('STOP')
