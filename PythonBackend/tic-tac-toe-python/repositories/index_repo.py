from abc import abstractmethod, ABC


# Since we've not yet stated officially that the option to create a player account is on the table, for now I am
# leaving that function out of the repository, but that can change when requested
class MainGameIndex (ABC):

    @abstractmethod
    def create_game(self, game):  # <- was originally create_player but need to see if that's
        pass                                      # a viable option

    @abstractmethod
    def get_game(self, g_id):
        pass

    @abstractmethod
    def update_game(self, game):
        pass

    @abstractmethod
    def delete_game(self, g_id):
        pass

    # @abstractmethod
    # def win_game(self, winner):  # <- was originally play_game, but I think this is the better defined function
    #     pass
    #
    # @abstractmethod
    # def end_game(self, is_finished):
    #     pass

    @abstractmethod
    def game_statistics(self, game_stats):
        pass
