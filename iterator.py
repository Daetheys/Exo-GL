class Stop(Exception):
    """ Exception to stop the computation """
    pass

class Search:
    def __init__(self,size,display):
        self._size = size
        self._display = display
        
        self.__col = [-1 for _ in range(size)]
        self.__up = [-1 for _ in range(2*size-1)]
        self.__down = [-1 for _ in range(2*size-1)]
        self._sol = []

    def nexti(self,i):
        """ Computes the next column position for queens """
        self.stop_check(i)
        for j in range(self._size):
            if self.__col[j] and self.__down[i+j] and self.__up[i-j+self._size-1]:
                self.__col[j] = self.__down[i+j] = self.__up [i-j+self._size-1] = False
                self._sol.append(j)
                self._display.aff_config(self._sol)
                self.nexti(i+1)
                self._sol.pop()
                self.__col[j] = self.__down[i+j] = self.__up [i-j+self._size-1] = True
                
    def stop_check(self,i):
        """ Check it the computation needs to stop (does nothing in Endless mode)"""
        pass

    def compute(self):
        """ Computes queens """
        self.nexti(0)
        self.end_compute()

    def end_compute(self):
        """ End the computation and show results """
        self._display.aff_message("No solution!")


class StopSearch(Search):
    """ Search mode that stops when the first solution is found """
    def compute(self):
        try:
            #Standard case : No solution found
            self.nexti(0)
            self.end_compute()
        except Stop:
            #A solution has eventually been found -> useless to call end_compute
            pass
        
    def stop_check(self,i):
        """ Check if a solution has been found """
        if i==self._size:
            self._display.aff_message("Solution found.")
            raise Stop()

class EndSearch(Search):
    """ End mode for computation and shows the number of solutions found """
    __nb = 0
    __bool = False #Reach bottom bool
        
    def stop_check(self,i):
        """ Count the number of solutions found """
        if i==self._size:
            self.__nb += 1
            self.__bool = True

    def end_compute(self):
        """ Print the number of solutions or no solutions """
        if self.__nb>0:
            self._display.aff_message(str(self.__nb)+" solutions found.")
        else:
            super().end_compute()
