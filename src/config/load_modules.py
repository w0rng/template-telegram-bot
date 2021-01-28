from os import walk
from . import dp


def load_modules(modules):
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


def load_middlewares(middlewares):
    for middleware in middlewares:
        *middleware, class_name = middleware.split('.')
        middleware = ".".join(middleware)
        middleware_module = __import__(f'middlewares.{middleware}')
        middleware_module = getattr(middleware_module, middleware)
        middleware_class = getattr(middleware_module, class_name)
        dp.middleware.setup(middleware_class())
