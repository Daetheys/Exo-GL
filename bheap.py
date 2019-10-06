# Ce fichier contient (au moins) cinq erreurs.
# Instructions:
#  - tester jusqu'à atteindre 100% de couverture;
#  - corriger les bugs;
#  - envoyer le diff ou le dépôt git par email.

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                #SWAP
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
                    
    def insert(self,k):
      self.heapList.append(k)
      self.percUp(self.currentSize)
      self.currentSize = self.currentSize + 1

    def percDown(self,i):
      while (i * 2) < self.currentSize: #On verifie qu'on n'est pas sur une feuille
          mc = self.minChild(i) #On prend le fils le plus petit
          if self.heapList[i] > self.heapList[mc]:
              #Swap
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
        if i * 2 + 1 >= self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.currentSize = self.currentSize - 1
      self.heapList[1] = self.heapList[self.currentSize]
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      #i = len(alist) #// 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      i = 1
      while (i <= self.currentSize):
          self.percUp(i)
          i = i + 1

#Pour un debug plus précis et rapide, permet de faire des tests au cas par cas au fur et a mesure du lancement des fonctions
if __name__ == "__main__":
    B = BinHeap()
    B.heapList = [0,0,-1,0,0,-1,0,0]
    for i in range(1,8):
        B.percUp(i)
        print("--")
