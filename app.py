from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

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