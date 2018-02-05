def percUp(self,i):
    while i//2 >0:
        if self.heapList[i] < self.heapList[i//2]:
            tmp=self.heapList[i//2]
            self.heapList[i//2]=self.heapList[i]
            self.heapList[i]=tmp
        i=i//2



def insert(self,k):
    self.heapList.append(k)
    self.currentsize=self.currentsize+1
    self.percUp(self.currentsize)

