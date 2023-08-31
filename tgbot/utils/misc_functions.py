# - *- coding: utf- 8 - *-
import asyncio
import json
from typing import Union

from aiogram import Dispatcher
from bs4 import BeautifulSoup

from tgbot.data.config import get_admins, BOT_VERSION, PATH_DATABASE
from tgbot.data.loader import bot
from tgbot.services.api_session import AsyncSession
from tgbot.utils.const_functions import get_unix, convert_day, get_date, ded


# Уведомление при запуске бота
async def startup_notify(dp: Dispatcher, rSession: AsyncSession):
    if len(get_admins()) >= 1:
        await send_admins(ded(f"""
                          <b>✅ Бот был успешно запущен</b>
                          ➖➖➖➖➖➖➖➖➖➖
                          <code>❗ Данное сообщение видят только администраторы бота.</code>
                          """),
                          markup="default")


# Рассылка сообщения всем администраторам
async def send_admins(message, markup=None, not_me=0):
    for admin in get_admins():

        try:
            if str(admin) != str(not_me):
                await bot.send_message(admin, message)
        except:
            pass
