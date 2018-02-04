def BinaryTree(r):
    return [r,[],[]]

def insertleft (root,newbranch):
    t=root.pop(1)

    if len(t)>1:
        root.insert(newbranch,t,[])
    else:
        root.insert(newbranch,[],[])
    return root

def insertright (root,newbranch):
    t=root.pop(2)

    if len(t)>1:
        root.insert(newbranch,[],t)
    else:
        root.insert(newbranch,[],[])
    return root

def getrootVal(root):
    return root[0]

def setrootVal(root,newval):
    root[0]==newval

def getleftchild(root):
    return root[1]
def getrightchild(root):
    return root[2]


