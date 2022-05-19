from abc import ABC

from repositories.index_repo import MainGameIndex
from models.index_model import MainGamePage


class MainGameRepoImpl(MainGameIndex):

    def create_game(self, game):
        pass

    def get_game(self, g_id):
        pass

    def update_game(self, game):
        pass

    def delete_game(self, g_id):
        pass

    def game_statistics(self, game_stats):
        pass