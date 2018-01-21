class Queues2stack :

    def __init__(self):
        #two queues taken

        self.instack=[]
        self.outstack=[]

    def enqueue(self,element):
        self.instack.append(element)
    def dequeue(self):

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()