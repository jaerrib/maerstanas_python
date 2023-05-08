from flask import Flask, render_template, redirect, session
from board import Board
from game_logic import valid_move, assign_move, change_player, check_score
app = Flask(__name__)
app.secret_key = "dev"

@app.route("/")
def index():
    if "board" not in session:
        board = Board()
        session["move_list"] = {}
        session["move_left"] = []
        session["score_p1"] = 0
        session["score_p2"] = 0
        session["result"] = ""
        session["active_player"] = 1
        session["board"] = board.data
    return render_template("index-alt.html",
                           board=session["board"],
                           score_p1=session["score_p1"],
                           score_p2=session["score_p2"] )

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    if valid_move(session["board"], row, col):
        session["board"] = assign_move(session["board"], row, col, session["active_player"])
        session["score_p1"] = check_score(session["board"], 1)
        session["score_p2"] = check_score(session["board"], 2)
        session["active_player"] = change_player(session["active_player"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)