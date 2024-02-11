from flask import Flask, render_template, redirect, session

from app.ai_player import get_best_move
from app.game import Game
from app.game_logic import valid_move, assign_move, change_stone

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def index():
    if "player2" not in session:
        session["player2"] = "computer"
    if "scoring" not in session:
        session["scoring"] = 1
    if "ruleset" not in session:
        session["ruleset"] = "0.4"
    if "data" not in session:
        game = Game()
        game.scoring_type = session["scoring"]
        game.ruleset = session["ruleset"]
        if game.ruleset == "0.2":
            game.special_stones["player1"] = [1]
            game.special_stones["player2"] = [1]
        session["data"] = {
            "move_list": game.move_list,
            "moves_left": game.moves_left,
            "score_p1": game.score_p1,
            "score_p2": game.score_p2,
            "result": game.result,
            "active_player": game.active_player,
            "active_stone": game.active_stone,
            "stone": game.stone,
            "board": game.board.data,
            "game_over": False,
            "player2": session["player2"],
            "scoring_type": game.scoring_type,
            "ruleset": game.ruleset,
            "special_stones": game.special_stones,
        }
    return render_template("index.html", data=session["data"])


@app.route("/new_game/<int:players>/<scoring_type>/<ruleset>")
def new_game(players, scoring_type, ruleset):
    session.clear()
    player_type = ["computer", "human"]
    session["player2"] = player_type[players - 1]
    if scoring_type == "simple":
        session["scoring"] = 0
    if ruleset == "02":
        session["ruleset"] = "0.2"
    else:
        session["ruleset"] = "0.4"
    return redirect("/")


@app.route("/reset")
def reset():
    session.pop("data")
    return redirect("/")


@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    if valid_move(session["data"], row, col):
        session["data"] = assign_move(session["data"], row, col)
    if (session["data"]["active_player"] == 2) and (
        session["data"]["player2"] == "computer"
    ):
        if len(session["data"]["moves_left"]):
            best_row, best_col = get_best_move(session["data"], sim_num=100, depth=49)
            session["data"] = assign_move(session["data"], best_row, best_col)
    session["data"]["game_over"] = session["data"]["moves_left"] == []
    return redirect("/")


@app.route("/stone/<int:player>/<int:stone>")
def stone_selector(player, stone):
    if (
        session["data"]["ruleset"] == "0.4"
        and session["data"]["active_player"] == player
    ):
        session["data"] = change_stone(session["data"], stone)
    return redirect("/")
