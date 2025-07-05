from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Get all deals')],
                                      [KeyboardButton(text='Get by name')],
                                      [KeyboardButton(text='Info from photo')]],
                           is_persistent=True,
                           resize_keyboard=True,
                           input_field_placeholder='Choose an option')

getByName = InlineKeyboardMarkup(inline_keyboard=
                              [[InlineKeyboardButton(text='Info', callback_data='info')],
                               [InlineKeyboardButton(text='Deals', callback_data='deals')]])

sites = InlineKeyboardMarkup(inline_keyboard=
                              [[InlineKeyboardButton(text='Marktplaats', callback_data="marktplaats")],
                               [InlineKeyboardButton(text='Reverb', callback_data='reverb')]])

show_more = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Show more', callback_data="marktplaats")]])