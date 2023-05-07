from flask import Flask, render_template, redirect, session
from board import Board
from game_logic import valid_move, assign_move
# from game import Game
app = Flask(__name__)
app.secret_key = "dev"

@app.route("/")
def index():
    # if "game" not in session:
    #     game = Game()
    if "board" not in session:
        board = Board()
        # session["move_list"] = game.move_list
        # session["move_left"] = game.move_left
        # session["score_p1"] = game.score_p1
        # session["score_p2"] = game.score_p2
        # session["result"] = game.result
        # session["active_player"] = game.active_player
        # session["board"] = game.board.data
        session["active_player"] = 1
        session["board"] = board.data
    return render_template("index-alt.html", board=session["board"])

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    if valid_move(session["board"], row, col):
        session["board"] = assign_move(session["board"], row, col, session["active_player"])
    print(session["board"])

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)