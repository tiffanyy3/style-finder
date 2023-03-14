from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

    # if "selection == blue/purple":
        # print("You are cool toned! Silver and rose gold jewelry look best on you. Styles in green, blue, purple, and black suit you well.")
    # if "selection == yellow/green":
        # print("You are warm toned! Gold jewelry looks best on you. Styles in red, orange, yellow, and brown suit you well.")
    # if "selection == I can't tell":
    # print("You are neutral toned! Everything suits you well! You can't go wrong with any color.")
@app.route("/results", methods=["GET","POST"])
def results():
    if request.method == "POST":
        place = request.form["place"]
        max_results = int(request.form["max_results"])
        radius = float(request.form["radius"])
        sort = "sort" in request.form
        results = functions.wikipedia_locationsearch(place,max_results=max_results,radius=radius,sort=sort)
        #return "Results that are close to {}".format(place)
        return render_template("results.html", results=results, place=place)
    else:
        return "Wrong HTTP method", 400