# Ce fichier contient (au moins) cinq erreurs.
# Instructions:
#  - tester jusqu'à atteindre 100% de couverture;
#  - corriger les bugs;
#  - envoyer le diff ou le dépôt git par email.

class EmptyHeap(Exception):
    pass

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 1
        
    #PRIVATE
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                #SWAP
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            	i = i // 2
            else:
            	break
            	
    def insert(self,k):
        self.heapList.append(k)
        self.percUp(self.currentSize)
        self.currentSize = self.currentSize + 1

    #PRIVATE
    def percDown(self,i):
        while (i * 2) < self.currentSize: #On verifie qu'on n'est pas sur une feuille
            mc = self.minChild(i) #On prend le fils le plus petit
            if self.heapList[i] > self.heapList[mc]:
                #Swap
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    #PRIVATE
    def minChild(self,i):
        if i * 2 + 1 >= self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
              return i * 2 + 1

    def delMin(self):
        if self.currentSize <= 1:
            raise EmptyHeap
        retval = self.heapList[1]
        self.currentSize = self.currentSize - 1
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
      #i = len(alist) #// 2
      self.currentSize = len(alist)+1
      self.heapList = [0] + alist[:]
      i = 1
      while (i <= self.currentSize-1):
          self.percUp(i)
          i = i + 1

