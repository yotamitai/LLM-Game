from flask import Flask, render_template, request, session
import random

from game.call_api import call_api, get_scenario

app = Flask(__name__)

# Set a secret key
app.secret_key = "M2vYPG#Lf2rSMWs$!Y"

# Initialize points
points = 0

@app.route("/", methods=["GET", "POST"])
def game():
    session["points"] = 0
    session["max_points"] = 0

    if request.method == "POST":
        choice = bool(request.form["choice"]) #TODO: change points based on choice
        scenario = get_scenario(test_scenario=True)

        # Update points based on the choice
        session["points"] += choice #TODO: edit points
        session["max_points"] = max(session["max_points"], session["points"])

        return render_template("game.html", scenario=scenario, points=points)
    return render_template("game.html", scenario=get_scenario(test_scenario=True), points=points)

@app.template_filter("enumerate")
def jinja2_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)

if __name__ == "__main__":
    app.run(debug=True)