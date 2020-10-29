from flask import Flask, render_template, request
from path_finder import Path_Finder
from functools import reduce



app = Flask(__name__)

pf = Path_Finder()

@app.route('/', methods = ['GET', 'POST'])
def path_display():


    return render_template("maze_display.html")


@app.route('/solve', methods = ['POST'])
def solve_maze():
    data = dict(request.form)

    pf.set_string_maze(data['arr'])
    pf.find_path()

    flat_locations = reduce(lambda z, y :z + y, reduce(lambda z, y :z + y, pf.locations.values()))
    return render_template("maze_display_solved.html", maze_solved=pf.array_maze, locations=flat_locations, final_path=pf.path)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
