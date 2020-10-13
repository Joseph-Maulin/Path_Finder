from flask import Flask, render_template
from path_finder import Path_Finder



app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def path_display():

    maze = "\n".join([
      ".W.F.." + ".W...." * 5,
      ".W...." * 6,
      ".W.WW." * 6,
      "....W." * 6,
      "....W." * 6,
      "....W." * 5 + "....W0"
    ])

    pf = Path_Finder(maze)
    pf.find_path()

    return render_template("maze_display.html", path_finder = pf)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
