#Check the two strings given to you are anagram or not.
#Anagram refers to the string whose letters are present in other string
#For example:- 'god' = 'dog' & 'clint eastwood' = 'old west action'




#FIRST SOLUTION
def anagram(s1,s2):

    s1=s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()
    if( sorted(s1)==sorted(s2)):
        print ("yes")
    else:
        print ("no")

anagram('dog','god')


#Second solution
def anagram2(s1,s2):

    s1=s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()

    #first check case if the lenght is not same of the same strings then it can not be a anagram
    if len(s1) != len(s2):
        return False

    #otherwise there is a possibility so
    count={}

    for letter in s1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1

    for letter in s2:
        if letter in count:
            count[letter]-=1
        else:
            count[letter]=1

    for k in count:
        if count[k]!=0:
            return False

    return True

anagram2('clint eastwood','old west action')