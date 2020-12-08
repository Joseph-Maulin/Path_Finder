# Path_Finder

# Introduction
An interactive path finding program to find the shortest distance between two points on a grid plane. It is a heroku hosted flask app using Python, Flask, and JQuery. Click the app below to view..

# App
https://path-finder-jm.herokuapp.com/

# What is here?
## path_finder.py
path_finder.py is used to solve the maze and find the shortest path. The maze is passed on a "\n" delimited string with "."s for open spaces and "W"s for walls. The passed maze string is then parsed and set up as an array with "0" in the staring position and "F" as the end marker. These default to upper left start and lower left finish if missing. A locations object is kept to store traversal data while solving the maze. The solver searches in steps by changing open blanks into the step number if available. Available open path search threads are kept in self.path_tracks. If no blank exists around a path head, that search thread is eliminated. If the "F" is found, that path thread is returned as a flattened row/col array.

## app.py
app.py is a simple flask app to display the interactive maze and to call the solved route result of the user constructed maze.

## templates/maze_display.html and templates/maze_solved.html
This uses JQuery, Jinja, Flask, Javascript, and CSS to display a user iteractive maze. The user draws a maze and places the start/finish markers to submit to find the shortest route to the finish. The program then displays the result to the user along with the process of the grid search in green. **Note that the display is artifically slowed down to be more visible to the human eye.
