from aiogram.types import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("🗳 Ovoz berish"),
        KeyboardButton("💰 Balans"),
        KeyboardButton("🔗 Referal ssilka"),
        KeyboardButton("📝 Qo'llanma"),
    )

    return btn


async def balance_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton("💳 Yechib olish"),
        KeyboardButton("🚫 Bekor qilish"),
    )

    return btn


async def referal_btn():
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        InlineKeyboardButton("Do'stlarni taklif qilish⤴️", callback_data="1")
    )

    return btn