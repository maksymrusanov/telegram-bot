from tg_bot.states import BotForm
from aiogram.fsm.context import FSMContext
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import tg_bot.keyboards as kb
from parser_main import main
from asyncio import to_thread
router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Search:', reply_markup=kb.start)


@router.callback_query(F.data == 'location')
async def enter_location(callback: CallbackQuery, state: FSMContext):
    await state.set_state(BotForm.location)
    await callback.message.answer('Enter your location:')
    await callback.answer()


@router.message(BotForm.location)
async def process_location(message: Message, state: FSMContext):
    location = message.text
    await state.update_data(location=message.text)
    location = await state.get_data()


@router.callback_query(F.data == 'budget')
async def enter_budget(callback: CallbackQuery, state: FSMContext):
    await state.set_state(BotForm.budget)
    await callback.message.answer('Enter your budget:')
    await callback.answer()


@router.message(BotForm.budget)
async def process_budget(message: Message, state: FSMContext):
    user_rent = message.text
    await state.update_data(budget=message.text)
    data = await state.get_data()
    location = data['location']
    budget = data['budget']
    main(location, budget)
