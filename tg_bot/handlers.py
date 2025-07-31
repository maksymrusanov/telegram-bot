from parser_folder.parse_session import ParserSession, user_sessions
from tg_bot.states import BotForm
from aiogram.fsm.context import FSMContext
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import tg_bot.keyboards as kb
import asyncio
import sys
import parser_folder.parser as parser
from parser_folder.db_utils import get_rows

router = Router()


@router.message(CommandStart())
async def start(message: Message, state):
    await state.set_state(BotForm.location)
    await message.answer('enter your location')


@router.message(BotForm.location)
async def enter_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await state.set_state(BotForm.budget)
    await message.answer('enter your budget')


@router.message(BotForm.budget)
async def enter_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    data = await state.get_data()

    user_id = message.from_user.id
    session = ParserSession(data["location"], data["budget"])
    user_sessions[user_id] = session

    session.parse_page()
    rows = get_rows()
    for row in rows:
        await message.answer(f"N {row[0]}\n{row[1]}\nPrice:{row[2]} GBP\nUrl:{row[3]}", parse_mode="HTML")

    await message.answer("choose your action", reply_markup=kb.nav_buttons)
    await state.clear()


@router.callback_query(F.data == "next")
async def handle_next_page(callback: CallbackQuery):
    user_id = callback.from_user.id
    session = user_sessions.get(user_id)

    if not session:
        await callback.message.answer("Session not found")
        return

    session.next_page()
    rows = get_rows(page=session.page)

    if not rows:
        await callback.message.answer("No more offers found.")
        return

    for row in rows:
        await callback.message.answer(
            f"N {row[0]}\n{row[1]}\nPrice:{row[2]} GBP\nUrl:{row[3]}",
            parse_mode="HTML"
        )

    await callback.message.answer("Choose your action", reply_markup=kb.nav_buttons)
    await callback.answer()


@router.callback_query(F.data == 'finish')
async def cmd_shutdown(callback: CallbackQuery):
    user_id = callback.from_user.id

    session = user_sessions.get(user_id)
    if session:
        session.close()
        del user_sessions[user_id]
    ParserSession.close
    parser.delete_db_file()
    await callback.message.answer('Bot stopped and DB deleted ')

    await callback.answer()
