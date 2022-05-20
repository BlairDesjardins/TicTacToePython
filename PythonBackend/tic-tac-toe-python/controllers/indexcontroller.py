from flask import jsonify

from errors.resourceNotfound import ResourceNotFound
from errors.resourceUnavailable import ResourceUnavailable
from models.index_model import MainGamePage
from implementations.index_repo_impl import MainGameRepoImpl
from services.index_services import MainGamePageServices


mr = MainGameRepoImpl()
ms = MainGamePageServices(mr)


def route(app):

    @app.route("/games", methods=['POST'])
    def create_game(game):
        try:
            body = request.json

            mr_request = ms.create_game(game(
                g_id=body["g_id"],
                x_player=body["x_player"],
                o_player=body["o_player"],
                game_stats=body["game_stats"],
                is_finished=body["is_finished"],
                winner=body["winner"]
            ))

            return jsonify(mr_request.json), 201
        except ResourceUnavailable as r:
            return r.message, 422

    @app.route("/games/<g_id>", methods=['GET'])
    def get_game(g_id):
        try:
            return jsonify(ms.get_game(g_id))
        except ValueError:
            return "Not a Valid Game Id", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/games/<g_id>", methods=['PUT'])
    def update_game(game):
        try:
            body = request.json

            mr_request = ms.update_game(game(
                g_id=body["g_id"],
                x_player=body["x_player"],
                o_player=body["o_player"],
                game_stats=body["game_stats"],
                is_finished=body["is_finished"],
                winner=body["winner"]
            ))

            return jsonify(mr_request)
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/games/<g_id>", methods=['DELETE'])
    def delete_game(g_id):
        try:
            ms.delete_game(g_id)
            return '', 204
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/games/<game_stats>", methods=['GET'])
    def game_statistics(game_stats):
        return jsonify()
