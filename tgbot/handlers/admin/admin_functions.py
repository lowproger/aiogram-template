# - *- coding: utf- 8 - *-

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.data.loader import dp, bot


# Рассылка
@dp.callback_query_handler(text="ok", state="*")
async def adm_new_user_cor(call: CallbackQuery, state: FSMContext):
	await bot.send_message(call.from_user.id, "Это оброботка инлайн кнопки!")
