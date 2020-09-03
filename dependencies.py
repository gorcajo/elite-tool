from injector import singleton

from service import RepairmentsService
from repository import DataBase, SqliteDataBase


def configure(binder):
    binder.bind(RepairmentsService, to=RepairmentsService, scope=singleton)
    binder.bind(DataBase, to=SqliteDataBase, scope=singleton)
    