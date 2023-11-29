from aiogram import executor, types, Dispatcher, Bot


BOT_TOKEN = "6765213772:AAEEn2qRXXFUJLcipSFmeZCUsYYNDkStWGY"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("hello welcome to my bot")


@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer("I help you")


@dp.message_handler(commands="photo")
async def start(message: types.Message):
    await message.answer_photo(photo="https://robocontest.uz/storage/uploads/profile/22107aGFtonSfMNqJptFxe1z8jAJt.jpg")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
