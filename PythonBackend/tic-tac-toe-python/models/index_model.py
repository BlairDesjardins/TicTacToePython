
class MainGamePage:
    def __init__(self, g_id, x_player, o_player, game_stats, is_finished, winner):
        self.g_id = g_id
        self.x_player = x_player
        self.o_player = o_player
        self.game_stats = game_stats
        self.is_finished = is_finished
        self.winner = winner

    def __repr__(self):
        return str({
            "g_id": self.g_id,
            "x_player": self.x_player,
            "o_player": self.o_player,
            "game_stats": self.game_stats,
            "is_finished": self.is_finished,
            "winner": self.winner
        })

    def __json_(self):
        return {
            "g_id": self.g_id,
            "x_player": self.x_player,
            "o_player": self.o_player,
            "game_stats": self.game_stats,
            "is_finished": self.is_finished,
            "winner": self.winner
        }
