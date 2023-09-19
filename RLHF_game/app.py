from flask import Flask, render_template, request, session
import random

from RLHF_game.call_api import call_api, get_scenario

app = Flask(__name__)

# Set a secret key
app.secret_key = "M2vYPG#Lf2rSMWs$!Y"

# Initialize points
points = 0

CONDITIONS = [
    "adversarial",
    "competitive",
    # "interactive"
]


@app.route("/", methods=["GET", "POST"])
def game():
    adversarial = competitive = interactive = False
    test_scenario = True

    if "adversarial" in CONDITIONS:
        if random.random() < 0.1:
            adversarial = True

    if "competitive" in CONDITIONS:
        competitive = True
        if session.get("points") is None:
            session["points"] = 0
        if session.get("max_points") is None:
            session["max_points"] = 0

    if "interactive" in CONDITIONS:
        interactive = True

    scenario = get_scenario(adversarial=adversarial, test_scenario=test_scenario)
    points = None if not competitive else session["points"]

    if request.method == "POST":
        choice = int(request.form["choice"])  # TODO: change points based on choice
        manual_text = request.form["text_response"] if interactive else None

        # Update points based on the choice
        if competitive:
            session["points"] += choice  # TODO: edit points
            session["max_points"] = max(session["max_points"], session["points"])
            points = session["points"]

        return render_template("game.html", scenario=scenario, points=points,
                               interactive=interactive)
    return render_template("game.html",
                           scenario=get_scenario(adversarial=adversarial, test_scenario=True),
                           points=points, interactive=interactive)


@app.template_filter("enumerate")
def jinja2_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)


if __name__ == "__main__":
    app.run(debug=True)
