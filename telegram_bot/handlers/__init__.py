from aiogram import Dispatcher

from .admin import register_admin
#from .base import register_base


def setup(dp: Dispatcher):
    register_admin(dp)