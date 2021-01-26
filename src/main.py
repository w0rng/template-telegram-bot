from loader import bot, dp
from data import config
from aiogram.utils.executor import start_polling, start_webhook
from utils.notify_admins import on_startup_notify, on_shutdown_notify


if __name__ == '__main__':
    if config.DOMAIN:
        bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)
        start_webhook(
            dispatcher=dp,
            webhook_path=config.WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup_notify,
            on_shutdown=on_shutdown_notify,
            host=config.WEBAPP_HOST,
            port=config.WEBAPP_PORT,
        )
    else:
        start_polling(
            dp,
            on_startup=on_startup_notify,
            on_shutdown=on_shutdown_notify,
            relax=1,
            timeout=20,
        )
