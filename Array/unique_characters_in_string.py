#check for if all the variables in the string are unique or duplicate
#for unique the function should return true else should return false


#First solution using in build method of python

def unique(s):
    return len(set(s))==len(s)


#Second solution
def unique(s):
    chars=set()

    for letters in set:
        if letters in chars:
            return False
        else:
            chars.add(letters)
    return True