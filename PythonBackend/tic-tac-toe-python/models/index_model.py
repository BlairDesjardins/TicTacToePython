
class MainGamePage:
    def __init__(self, g_id=0, x_player=0, o_player=0, current_player=0, game_state=",,,,,,,,", is_finished=False,
                 winner=None):  # ^ Here you are implementing key variables to your values to create a game
        self.g_id = g_id
        self.x_player = x_player
        self.o_player = o_player
        self.current_player = current_player
        self.game_state = game_state
        self.is_finished = is_finished
        self.winner = winner

    def __repr__(self):
        return str({
            "g_id": self.g_id,
            "x_player": self.x_player,
            "o_player": self.o_player,
            "current_player": self.current_player,
            "game_state": self.game_state,
            "is_finished": self.is_finished,
            "winner": self.winner
        })

    def json(self):  # <- Pay close attention to your json constructor, do not include underscores ( __ )
        return {
            "gId": self.g_id,
            "xPlayer": self.x_player,
            "oPlayer": self.o_player,
            "currentPlayer": self.current_player,
            "gameState": self.game_state,
            "isFinished": self.is_finished,
            "winner": self.winner
        }
