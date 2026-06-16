from aiogram import Router, types
from aiogram.filters import Command, CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот-помощник.\n"
        "Команды: /help — список команд"
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — начать\n"
        "/help — это сообщение\n"
        "/next_race - следущая гонка\n"
        "/standings - таблица лидеров"
    )