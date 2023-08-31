# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.data.loader import dp


####################################################################################################
############################################## ПРОЧЕЕ ##############################################
# Открытие главного меню
@dp.message_handler(text=['🔙 Главное меню', '/start'], state="*")
async def main_start(message: Message, state: FSMContext):
	await state.finish()
	await message.answer("Привет, введи свое имя")
	await state.set_state("new_user")


@dp.message_handler(state="new_user")
async def reg_new_user(message: Message, state: FSMContext):
	await state.finish()
	await message.answer(f"Привет, {message.text}")
