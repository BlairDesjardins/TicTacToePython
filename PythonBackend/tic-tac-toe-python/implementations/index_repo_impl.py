from abc import ABC
from errors.resourceNotfound import ResourceNotFound
from util.db_connection import connection
from repositories.index_repo import MainGameIndex
from models.index_model import MainGamePage


def _build_game(game_record):
    return MainGamePage(g_id=int(game_record[0]), x_player=game_record[1], o_player=game_record[2],
                        game_stats=game_record[3], is_finished=game_record[4], winner=game_record[5])


class MainGameRepoImpl(MainGameIndex):

    def create_game(self, game):
        sql = "INSERT INTO games VALUES (DEFAULT, %s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()

        cursor.execute(sql, [game.g_id, game.x_player, game.o_player, game.game_stats, game.is_finished,
                             game.winner])

        connection.commit()
        record = cursor.fetchone()

        return _build_game(record)

    def get_game(self, g_id):
        sql = "SELECT * FROM games WHERE g_id = %s"
        cursor = connection.cursor()

        cursor.execute(sql, g_id)

        record = cursor.fetchone()
        if record:
            return _build_game(record)
        else:
            raise ResourceNotFound(f"Requested Game with ID: {g_id} cannot found")

    def update_game(self, game):
        sql = "UPDATE games SET g_id=%s, x_player=%s, o_player=%s, game_stats=%s, is_finished=%s, winner=%s RETURNING *"
        cursor = connection.cursor()

        cursor.execute(sql, [game.g_id, game.x_player, game.o_player, game.game_stats, game.is_finished, game.winner])

        connection.commit()
        record = cursor.fetchone()
        if record:
            return _build_game(record)
        else:
            raise ResourceNotFound(f"Requested Game with ID: {game.g_id} cannot found")

    def delete_game(self, g_id):
        sql = "DELETE FROM games WHERE g_id=%s RETURNING *"
        cursor = connection.cursor()

        cursor.execute(sql, g_id)

        connection.commit()
        record = cursor.fetchone()
        if record:
            return _build_game(record)
        else:
            raise ResourceNotFound(f"Requested Game with ID: {g_id} cannot be found")

    def game_statistics(self, game_stats):
        sql = "SELECT * FROM games"
        cursor = connection.cursor()

        cursor.execute(sql, game_stats)

        records = cursor.fetchall()

        return [MainGamePage()]


if __name__ == '__main__':
    mr = MainGameRepoImpl()
    print(mr.game_statistics())
