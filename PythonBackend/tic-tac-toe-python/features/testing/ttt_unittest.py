import unittest
from unittest.mock import MagicMock

from models.index_model import MainGamePage
from implementations.index_repo_impl import MainGameRepoImpl
from services.index_services import MainGamePageServices


class TestMainGamePageServices(unittest.TestCase):
    mr = MainGameRepoImpl()
    ms = MainGamePageServices(mr)

    game = MainGamePage()
    created_game = MainGamePage()
    delete_game = MainGamePage()

    @classmethod
    def setUpClass(cls):
        new_game = MainGamePage(g_id=1, x_player=1, o_player=2, current_player=1, game_state=",,,,,,,,",
                                is_finished=False, winner=None)
        cls.game = cls.ms.create_game(new_game)

        cls.delete_game = cls.ms.create_game(
            MainGamePage(g_id=1, x_player=1, o_player=2, current_player=1, game_state=",,,,,,,,",
                         is_finished=False, winner=None))

    @classmethod
    def tearDownClass(cls):
        cls.ms.delete_game(cls.game.g_id)
        cls.ms.delete_game(cls.created_game.g_id)

    def test_create_game(self):
        TestMainGamePageServices.created_game = self.ms.create_game(MainGamePage(g_id=1, x_player=1, o_player=2,
                                                                                 current_player=1,
                                                                                 game_state=",,,,,,,,",
                                                                                 is_finished=False, winner=None))

        self.assertEqual(self.created_game, MainGamePage(g_id=self.created_game.g_id, x_player=1, o_player=2,
                                                         current_player=1, game_state=",,,,,,,,", is_finished=False,
                                                         winner=None))

    def test_get_game(self):
        returned_game = self.ms.get_game(self.game.g_id)

        self.assertEqual(returned_game, self.game)

    def test_get_current_game(self):
        self.ms.index_repo.get_all_games_by_id = MagicMock(return_value=[
            MainGamePage(g_id=1, x_player=1, o_player=2, current_player=1, game_state=",,,,,,,,",
                         is_finished=False, winner=None),
            MainGamePage(g_id=1, x_player=1, o_player=3, current_player=1, game_state=",,,,,,,,",
                         is_finished=False, winner=None)
        ])

        games_by_id = self.ms.get_current_game(2)

        self.assertEqual(games_by_id,
                         MainGamePage(g_id=1, x_player=1, o_player=2, current_player=1, game_state=",,,,,,,,",
                                      is_finished=False, winner=None))

    def test_update_game(self):
        self.game = self.ms.update_game(MainGamePage(g_id=self.game.g_id, x_player=1, o_player=2,
                                                     current_player=2, game_state="X,,,,,,,,",
                                                     is_finished=False, winner=None))

        self.assertEqual(self.game, MainGamePage(g_id=self.game.g_id, x_player=1, o_player=2, current_player=2,
                                                 game_state="X,,,,,,,,", is_finished=False, winner=None))

    def test_delete_game(self):
        self.assertIsNotNone(self.ms.delete_game(self.delete_game.g_id))


if __name__ == '__main__':
    unittest.main()
