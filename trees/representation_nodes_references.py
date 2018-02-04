class BinaryTree(object):

    def __init(self,rootObj):

        self.key=rootObj
        self.LeftChild=None
        self.RightChild=None

    def insertleft(self,newnode):
        if self.LeftChild==None:
            self.LeftChild = BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.LeftChild=self.LeftChild
            self.LeftChild=t

    def insertright(self,newnode):
        if self.RightChild==None:
            self.RightChild = BinaryTree(newnode)
        else:
            t=BinaryTree(newnode)
            t.RightChild=self.RightChild
            self.RightChild=t

    def getrightChild(self):
        return self.RightChild

    def getleftChild(self):
        return self.LeftChild
    def setrootVal (self,obj):
        self.key=obj

    def getrootVal(self):
        return self.key

