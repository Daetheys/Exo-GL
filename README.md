# Exo-GL
Exercices de test de GL

There are 3 files : Graphics.py handles graphic output of results (O for Terminal and G for pygame window).
                    iterator.py is the file containing the algorithm reponsible for different styles of computations (S for stop to the first and E for count the number of solutions)
                    queens.py is the main file to run
                    
Here is the theoritical model to execute the code :
  python queens.py [n] (G/O) (E/S)
    where [n] is the size of the board -default value is 7- , (G/O) are graphical options -default value is O- and (E/S) are computations options -default value is S-
    
Examples : 
  python queens.py 10 G E
  python queens.py 8 O
  python queens.py 4
  python queens.py
