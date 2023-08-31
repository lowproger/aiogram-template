# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Инлайн кнопка
ok_kb = InlineKeyboardMarkup(
).add(
	InlineKeyboardButton("✅ ОК", callback_data=f"ok")
)
