from flask import Flask, render_template, redirect, session
from game import Game
from game_logic import valid_move, assign_move, change_player, update_score
app = Flask(__name__)
app.secret_key = "dev"

@app.route("/")
def index():
    if "player2" not in session:
            session["player2"] = "human"
    if "data" not in session:
        game = Game()
        session["data"] = {
            "move_list": game.move_list,
            "moves_left": game.moves_left,
            "score_p1": game.score_p1,
            "score_p2": game.score_p2,
            "result": game.result,
            "active_player": game.active_player,
            "board": game.board.data,
            "game_over": False,
            "player2": session["player2"]
        }
    return render_template("index.html", data=session["data"])

@app.route("/new_game/2")
def new_two_player_game():
    session.clear()
    session["player2"] = "human"
    return redirect("/")


@app.route("/new_game/1")
def new_one_player_game():
    session.clear()
    session["player2"] = "computer"
    return redirect("/")


@app.route("/reset")
def reset():
    session.pop("data")
    return redirect("/")

@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    if valid_move(session["data"], row, col):
        session["data"] = assign_move(session["data"], row, col)
    session["data"]["game_over"] = session["data"]["moves_left"] == []
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)