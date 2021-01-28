from .installed_modules import INSTALLED_MODULES, INSTALLED_MIDLEWARES
from .environ import *
from .bot import *
from .load_modules import load_modules, load_middlewares


load_modules(INSTALLED_MODULES)
load_middlewares(INSTALLED_MIDLEWARES)
