import time
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def com_start(message: Message):
    print(message.from_user.id)
    await message.answer('Привет!', reply_markup=kb.main)
