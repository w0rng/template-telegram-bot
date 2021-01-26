from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from os import walk
from data import config


bot = Bot(token=config.TG_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Инициализация модулей
modules = [
    'middlewares',
    'filters',
    'handlers'
]

for module in modules:
    for i in walk(f'src/{module}'):
        directory, paths, files = i
        directory = '.'.join(directory.split('/')[1:])
        if '__init__.py' in files:
            __import__(directory)
            files.remove('__init__.py')
        for file in files:
            file_name, *_,  ext = file.split('.')
            if len(_) or ext != 'py':
                continue
            __import__(f'{directory}.{file_name}')
