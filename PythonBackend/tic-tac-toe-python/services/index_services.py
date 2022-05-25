
from errors.resourceUnavailable import ResourceUnavailable

from repositories.index_repo import MainGameIndex
from implementations.index_repo_impl import MainGameRepoImpl


class MainGamePageServices:

    def __init__(self, index_repo: MainGameIndex):
        self.index_repo = index_repo

    def create_game(self, game):
        return self.index_repo.create_game(game)

    def get_game(self, g_id):
        return self.index_repo.get_game(g_id)

    def get_all_games_by_id(self, u_id):
        return self.index_repo.get_all_games_by_id(u_id)

    def get_current_game(self, u_id):
        games = self.index_repo.get_all_games_by_id(u_id)
        filtered = list(filter(lambda game: game.o_player == u_id and not game.is_finished, games))
        if len(filtered) == 0:  # <- here you are referencing the list (filtered) length
            raise ResourceUnavailable(f"User Id {u_id} is not found")
        return filtered[0]

    def update_game(self, game):
        return self.index_repo.update_game(game)

    def delete_game(self, g_id):
        return self.index_repo.delete_game(g_id)

    def update_game_state(self, g_id, game_state, current_player, is_finished, winner):
        game = self.get_game(g_id)  # <- Working something similar to a constructor
        game.game_state = game_state
        game.current_player = current_player
        game.is_finished = is_finished
        game.winner = winner
        self.update_game(game)
        return game


if __name__ == '__main__':
    mr = MainGameRepoImpl()
    ms = MainGamePageServices(mr)
    mr.update_game(1)
