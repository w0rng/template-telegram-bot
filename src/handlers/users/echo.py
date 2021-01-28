from aiogram import types
from config import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(
        f"Эхо без состояния.\nСообщение: {message.text}"
    )
