from flask import Flask, render_template, redirect, session
from app.game import Game
from app.game_logic import valid_move, assign_move
from app.ai_player import get_best_move

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def index():
    if "player2" not in session:
        session["player2"] = "computer"
    if "scoring" not in session:
        session["scoring"] = 1
    if "data" not in session:
        game = Game()
        game.scoring_type = session["scoring"]
        session["data"] = {
            "move_list": game.move_list,
            "moves_left": game.moves_left,
            "score_p1": game.score_p1,
            "score_p2": game.score_p2,
            "result": game.result,
            "active_player": game.active_player,
            "board": game.board.data,
            "game_over": False,
            "player2": session["player2"],
            "scoring_type": game.scoring_type,
        }
    return render_template("index.html", data=session["data"])


@app.route("/new_game/<int:players>/<scoring_type>")
def new_game(players, scoring_type):
    session.clear()
    player_type = ["computer", "human"]
    session["player2"] = player_type[players - 1]
    if scoring_type == "simple":
        session["scoring"] = 0
    return redirect("/")


@app.route("/reset")
def reset():
    session.pop("data")
    return redirect("/")


@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    if valid_move(session["data"], row, col):
        session["data"] = assign_move(session["data"], row, col)
    if ((session["data"]["active_player"] == 2) and
            (session["data"]["player2"] == "computer")):
        if len(session["data"]["moves_left"]):
            best_row, best_col = get_best_move(
                session["data"],
                sim_num=100,
                depth=49)
            session["data"] = assign_move(session["data"], best_row, best_col)
    session["data"]["game_over"] = session["data"]["moves_left"] == []
    return redirect("/")


@app.route("/move/<int:row>/<int:col>")
def move(row, col):
    if valid_move(session["data"], row, col):
        stone_color = ["dark_stone", "light_stone"]
        stone = stone_color[session["data"]["active_player"] - 1]
        stone_string = f"""
        <img src = "static/img/{stone}.svg" class ="stone" alt = "{stone}">
        """
        session["data"] = assign_move(session["data"], row, col)
        session["data"]["game_over"] = session["data"]["moves_left"] == []
        response = stone_string
        return response
    return None


