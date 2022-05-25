from flask import jsonify, request

from errors.resourceNotfound import ResourceNotFound
from errors.resourceUnavailable import ResourceUnavailable
from models.index_model import MainGamePage
from implementations.index_repo_impl import MainGameRepoImpl
from services.index_services import MainGamePageServices


mr = MainGameRepoImpl()
ms = MainGamePageServices(mr)


def route(app):

    @app.route("/games", methods=['POST'])
    def create_game():
        try:
            body = request.json

            mr_game = ms.create_game(MainGamePage(  # <-the model index is referenced here
                x_player=body["xPlayer"],  # <-all variables are to be done in camelCase for JSON
                o_player=body["oPlayer"],
                current_player=body["currentPlayer"],
                game_state=body["gameState"],
                is_finished=body["isFinished"],
                winner=body["winner"]
            ))

            return jsonify(mr_game.json()), 201
        except ResourceUnavailable as r:
            return r.message, 422

    @app.route("/games/<g_id>", methods=['GET'])
    def get_game(g_id):
        try:
            return jsonify(ms.get_game(g_id).json())
        except ValueError:
            return "Not a Valid Game Id", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/games/history/<u_id>", methods=['GET'])
    def get_all_games_by_id(u_id):
        return jsonify([game.json() for game in ms.get_all_games_by_id(u_id)])

    @app.route("/games/users/<u_id>", methods=['GET'])
    def get_current_game(u_id):  # the u_id is not in our models page, but rather in our database
        try:
            return jsonify(ms.get_current_game(int(u_id)).json())
        except ResourceUnavailable as e:
            return e.message, 404

    @app.route("/games/<g_id>", methods=['PUT'])
    def update_game(g_id):
        try:
            body = request.json  # <- this is a json object

            mr_game = ms.update_game(MainGamePage(  # <- the model index is referenced here
                g_id=g_id,  # <this needs to be its own value
                x_player=body["xPlayer"],
                o_player=body["oPlayer"],
                current_player=body["currentPlayer"],
                game_state=body["gameState"],
                is_finished=body["isFinished"],
                winner=body["winner"]
            ))

            return jsonify(mr_game.json())  # <the .json() object serializes the catch into a JSON object
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/games/<g_id>", methods=['DELETE'])
    def delete_game(g_id):
        try:
            ms.delete_game(g_id)
            return '', 204
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/games/<g_id>", methods=['PATCH'])
    def update_game_state(g_id):
        body = request.json

        try:
            g = ms.update_game_state(g_id, body["gameState"], body["currentPlayer"], body["isFinished"],
                                     body["winner"])  # You'll want this to match your Postman Attributes
            return g.json()                           # in your PATCH request
        except ResourceNotFound as r:
            return r.message, 404
