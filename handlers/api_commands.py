import logging
from aiogram import Router, types
from aiogram.filters import Command
from services import f1_api

router = Router()
logger = logging.getLogger(__name__)


@router.message(Command("next_race"))
async def cmd_next_race(message: types.Message):
    try:
        race = await f1_api.get_next_race()
        text = (
            f"🏎 Следующая гонка: {race['name']}\n"
            f"📍 {race['circuit']}, {race['country']}\n"
            f"📅 {race['date']} в {race['time']}"
        )
        await message.answer(text)
    except Exception:
        logger.exception("Ошибка при получении данных о гонке")
        await message.answer("Не получилось получить данные о гонке 😔 Попробуй позже.")


@router.message(Command("standings"))
async def cmd_standings(message: types.Message):
    try:
        standings = await f1_api.get_driver_standings(top_n=5)
        lines = ["🏆 Топ-5 личного зачёта:"]
        for s in standings:
            lines.append(f"{s['position']}. {s['name']} — {s['points']} очков")
        await message.answer("\n".join(lines))
    except Exception:
        logger.exception("Ошибка при получении турнирной таблицы")
        await message.answer("Не получилось получить таблицу 😔")