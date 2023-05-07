from flask import Flask, render_template, redirect, session
from board import Board
app = Flask(__name__)
app.secret_key = "dev"

@app.route("/")
def index():
    if "board" not in session:
        board = Board()
        session["board"] = board.data
    return render_template("index-alt.html", board=session["board"])

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    print(f"Last move: {row}, {col}")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)