from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


button_start = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="correct your favourite team")],
                [KeyboardButton(text="upcoming match for your favourite teams")],
                [KeyboardButton(text="started matches"),  KeyboardButton(text="match results")],
                    ],
            resize_keyboard=True
)


button_correct_your_favourite_team = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="add team"), KeyboardButton(text="delete team")],
                [KeyboardButton(text="exit")]
                    ],
            resize_keyboard=True
)
