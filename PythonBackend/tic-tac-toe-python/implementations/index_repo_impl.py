
from errors.resourceNotfound import ResourceNotFound
from util.db_connection import connection
from repositories.index_repo import MainGameIndex
from models.index_model import MainGamePage


def _build_game(game_record):
    return MainGamePage(g_id=int(game_record[0]), x_player=game_record[1], o_player=game_record[2],
                        game_state=game_record[3], is_finished=game_record[4], winner=game_record[5],
                        current_player=game_record[6])


class MainGameRepoImpl(MainGameIndex):

    def create_game(self, game):
        sql = "INSERT INTO games VALUES (DEFAULT, %s, %s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()

        cursor.execute(sql, [game.x_player, game.o_player, game.game_state, game.is_finished,
                             game.winner, game.current_player])

        connection.commit()
        record = cursor.fetchone()

        return _build_game(record)

    def get_game(self, g_id):
        sql = "SELECT * FROM games WHERE g_id = %s"
        cursor = connection.cursor()

        cursor.execute(sql, [g_id])

        connection.commit()
        record = cursor.fetchone()
        if record:
            return _build_game(record)
        else:
            raise ResourceNotFound(f"Requested Game with ID: {g_id} cannot be found")

    def get_all_games_by_id(self, u_id):
        sql = "SELECT * FROM games WHERE x_player=%s OR o_player=%s"
        cursor = connection.cursor()

        cursor.execute(sql, [u_id, u_id])  # <- since both X and O players are being referenced in the function,
        #                                       they each need their own individual user_id tag

        connection.commit()
        records = cursor.fetchall()

        return [_build_game(record) for record in records]

    def update_game(self, game):
        sql = "UPDATE games SET x_player=%s, o_player=%s, game_state=%s, is_finished=%s, winner=%s, current_player=%s "\
              "WHERE g_id=%s RETURNING *"
        cursor = connection.cursor()

        cursor.execute(sql, [game.x_player, game.o_player, game.game_state, game.is_finished, game.winner,
                             game.current_player, game.g_id])

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

    # def update_game_state(self, game_state):
    #     sql = "SELECT * FROM games"
    #     cursor = connection.cursor()
    #
    #     cursor.execute(sql, game_state)
    #
    #     connection.commit()
    #     records = cursor.fetchall()
    #
    #     return


if __name__ == '__main__':
    mr = MainGameRepoImpl()
    print()
