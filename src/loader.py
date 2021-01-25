from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_polling, start_webhook
from utils.notify_admins import on_startup_notify, on_shutdown_notify

from data import config


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def polling():
    start_polling(
        dp,
        on_startup=on_startup_notify,
        on_shutdown=on_shutdown_notify,
        relax=1,
        timeout=20,
    )


def webhook():
    start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup_notify,
        on_shutdown=on_shutdown_notify,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
    )


starter = webhook if config.DOMAIN else polling


if config.DOMAIN:
    bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)
