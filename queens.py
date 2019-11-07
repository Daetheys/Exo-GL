#!/usr/bin/python3

# A solver for the n-queens problem
#
# It uses a recursive search algorithm with backtracking,
# and displays naively the current partial solution.
#
# Some background information on Wikipedia:
#   https://en.wikipedia.org/wiki/Eight_queens_puzzle
#
# Question 1
# ----------
# Modify the code to add a more graphical display of the current
# partial solution, using pygame [1] or curses [2].
# The "old" display should remain available and the search
# algorithm should not be duplicated. More specifically,
# search(size,G) should start the search with a graphical progress
# display, and start(size,O) should do the same with the old
# display, for some G and O. The two modes should be available to
# the user via the command-line.
#
# [1] https://docs.python.org/3/howto/curses.html
# [2] https://www.pygame.org/
#
# Question 2
# ----------
# Modify the procedure so that it also allows to obtain
# the number of solutions instead of printing and exiting
# after having found the first solution.
# It should still be possible to obtain the old behaviour
# (which avoids exploring the whole solution space).
# The two modes should be available to the user via the
# command-line.
# Bonus points if other interesting uses are enabled by the
# modified procedure.

from Graphics import *
from iterator import *
import sys
size = 7
if len(sys.argv)>1:
    try:
        size = int(sys.argv[1])
    except (IndexError,ValueError):
        display.aff_error("Usage: %s <int>" % sys.argv[0])
        exit(1)
#Create the Display object according to the second given arg
if len(sys.argv)>2:
    try:
        display_mode = sys.argv[2]
    except (IndexError,ValueError):
        #By default the mode is Terminal
        display_mode = "O"
    display = Terminal(size)
    if display_mode == "G":
        display = Window(size,0,1)
    elif display_mode != "O":
        display.aff_error("Wrong second arg : %s, should be 'G' for a windowed output and 'O' for a terminal one")
        exit(1)
#Create the Search object according to the third given arg
if len(sys.argv)>3:
    try:
        compute_mode = sys.argv[3]
    except (IndexError,ValueError):
        #By default the mode is Stop
        compute_mode = "S"
    searchway = StopSearch(size,display)
    if compute_mode == "E":
        searchway = EndSearch(size,display)
    elif compute_mode != "S":
        display.aff_error("Wrong third arg : %s, should be 'S' for a stop computation and 'E' for the complete one")
        exit(1)
#Default modes if there is not enough parameters
if len(sys.argv)<=2:
    display = Terminal(size)
if len(sys.argv)<=3:
    searchway = StopSearch(size,display)
#Start the procedure
display.aff_message("Searching for size %d..." % size)
searchway.compute()
display.aff_loop()
