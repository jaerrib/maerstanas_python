from flask import Flask, render_template, redirect, session
from app.game import Game
from app.game_logic import valid_move, assign_move, convert_num_to_row
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
        game = Game(9)
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
        session["data"] = assign_move(session["data"], row, col)
        score_p1 = session["data"]["score_p1"]
        score_p2 = session["data"]["score_p2"]
        moves_left = session["data"]["moves_left"]
        session["data"]["game_over"] = len(moves_left) == 0
        stone_string = f"""
        <img src = "static/img/{stone}.svg" class ="stone" alt = "{stone}">
        """
        score_string = f"""
        <div id="score" hx-swap-oob="true" class="d-flex mt-1">
            <p class="ps-2 text-body-emphasis fs-4 mb-0">Player 1: {score_p1}</p>
            <p class="ps-4 text-body-emphasis fs-4 mb-0">Player 2: {score_p2}</p>
        </div>
        """
        move_string = f'<div id="moves" hx-swap-oob="true">'
        if session["data"]["game_over"]:
            move_string += f'<p class="fs-4 text-info fw-bold">GAME OVER</p>'
        counter = 1
        reverse_move_list = reversed(session["data"]["move_list"])
        for each_move in reverse_move_list:
            move_num = len(session["data"]["move_list"]) - counter + 1
            move_string += f"""
                <p>
                    <span class="text-secondary">{move_num}.</span>
                    {each_move[1]} (Player {each_move[0]})
                </p>
            """
            counter += 1
        move_string += f"</div>"
        response = stone_string + score_string + move_string
        return response
    else:
        # row_char = convert_num_to_row(row)
        # response = f"""
        # <div id="errors" hx-swap-oob="true" class="text-danger fs=4">{row_char}{col} is an illegal move</div>
        # """
        return None


@app.route("/build-board")
def build_board():
    game_area = '<div id="game_area">'

    letter_area = f"""
        <!-- Letter Row -->
            <div class="d-flex">
            <div class="square"></div>
    """
    for row in range(1, len(session["data"]) - 2):
        row_char = convert_num_to_row(row)
        letter_area += f'<div class="square">{row_char}</div>'
    letter_area += "</div>"
    board_area = f"""
        
    """
    for row in range(1, len(session["data"]) - 2):
        board_area += f"""
            <div class="d-flex">
                <div class="square">{row}</div>
        """
        for col in range(1, len(session["data"]) - 2):
            board_area += f"""
                <div class="square bg-secondary border border-secondary-subtle" hx-get="/move/{row}/{col}" hx-swap="innerHTML">
            """
            board_val = session["data"]["board"][row][col]
            if 0 < board_val < 3:
                stone_color = ["dark_stone", "light_stone"]
                stone = stone_color[session["data"]["board"][row][col] - 1]
                board_area += f"""
                <img src = "static/img/{stone}.svg" class ="stone" alt = "{stone}">
                """
            board_area += "</div>"
        board_area += "</div>"

    response = game_area + letter_area + board_area + "</div>"
    return response
