from flask import Flask, render_template
from path_finder import Path_Finder



app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def path_display():

    pf = Path_Finder()

    return render_template("maze_display.html", path_finder = pf)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
