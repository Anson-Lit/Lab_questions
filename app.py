from flask import Flask, request
from models.score_manager import ScoreManager
from models.score import Score


app = Flask(__name__)
score_manager = ScoreManager()


@app.route('/api/list')
def list_all_scores():
    return {"scores": score_manager.get_scores()}


@app.route('/api/new', methods=["PUT"])
def add_new_score():
    try:
        #-- get the JSON data of the request, containing a new object to add
        data = request.get_json()
        # do some work to add a new score to the score manager
        return "", 204
    except:
        return "Invalid data provided.", 400


if __name__ == "__main__":
    print("hi")
    app.run()