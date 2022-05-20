
from errors.resourceUnavailable import ResourceUnavailable

from repositories.index_repo import MainGameIndex
from implementations.index_repo_impl import MainGameRepoImpl


class MainGamePageServices:

    def __init__(self, index_repo: MainGameIndex):
        self.index_repo = index_repo

    def create_game(self, game):
        available =
        if available <= 0:
            raise ResourceUnavailable(f"Game is unavailable at this time")

        return self.index_repo.create_game(game)

    def get_game(self, g_id):
        return self.index_repo.get_game(g_id)

    def update_game(self, game):
        return self.index_repo.update_game(game)

    def delete_game(self, g_id):
        return self.index_repo.delete_game(g_id)

    def game_statistics(self, game_stats):
        return self.index_repo.game_statistics(game_stats)

if __name__ == '__main__':
    mr = MainGameRepoImpl()
    ms = MainGamePageServices(mr)
    mr.game_statistics(1)
