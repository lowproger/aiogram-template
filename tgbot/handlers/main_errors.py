# - *- coding: utf- 8 - *-
from aiogram.types import Update

from tgbot.data.loader import dp
from tgbot.utils.misc.bot_logging import bot_logger


# Обработка телеграм ошибок
@dp.errors_handler()
async def main_errors(update: Update, exception):
    print(f"-Exception | {exception}")
    bot_logger.exception(
        f"Exception: {exception}\n"
        f"Update: {update}"
    )
