from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram import F

import buttons
from parser import getItems
from states import States

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("🎸 Hey! What are we doing today?", reply_markup=buttons.main)


@router.message(F.text == "Get all deals")
async def deals(message: Message, state: FSMContext):
    await message.answer("Enter minimum price\n(or 0 for none)")
    await state.set_state(States.min_price)


@router.message(States.min_price)
async def min_price(message: Message, state: FSMContext):
    await state.update_data(min_price=message.text)
    await message.answer("Enter maximum price\n(or 0 for none)")
    await state.set_state(States.max_price)


@router.message(States.max_price)
async def min_price(message: Message, state: FSMContext):
    await state.update_data(max_price=message.text)
    data = await state.get_data()
    print(data)
    await state.clear()
    await message.answer("Which site do you want to get deals from?", reply_markup=buttons.sites)


@router.callback_query(F.data == "marktplaats")
async def marktplaats(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    offset = data.get("offset", 0)
    items = getItems(offset = offset)

    if not items:
        await callback.message.answer("No more items found.")
        await callback.answer()
        return

    items = [items[0], items[1], items[2]]
    for item in items:
        await callback.message.answer_photo(photo=item["img"],
                                            caption=f"🎸{item['title']}\n💶 €{item['price']}\nLink: {item['url']}")

    # Update offset for next call
    await state.update_data(offset=offset + 30)
    await callback.message.answer("👇", reply_markup=buttons.show_more)
    await callback.answer()


@router.message(F.text == "Get by name")
async def deals(message: Message, state: FSMContext):
    await message.answer("Enter the name of guitar")
    await state.set_state(States.guitar_name)


@router.message(States.guitar_name)
async def handle_guitar_name(message: Message, state: FSMContext):
    await state.update_data(guitar_name=message.text)
    data = await state.get_data()
    await message.answer(f'Entered name: {data["guitar_name"]}')
    await state.clear()


@router.message(F.text == "lookup")
async def getByName(message: Message):
    await message.answer("Choose an option", reply_markup=buttons.getByName)


@router.callback_query(F.data == 'info')
async def info(callback: CallbackQuery):
    await callback.message.answer('Here\'s info about this guitar: \n')
    await callback.answer()


@router.message()
async def unknown_message_handler(message: Message):
    await message.answer("❌ Sorry, I didn't understand that. Type /start to see available options.")
