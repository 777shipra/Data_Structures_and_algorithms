#in missing element problem u would be given with two array . first array will contain numbers and second arrar will
#contained shuffled and some deleted numbers from the first array
#find and type the missing element

#first solution
def finder(arr1,arr2):
    #sorting the arrays first
    arr1.sort()
    arr2.sort()
    #zip means [1,2,3] and [4,5,6]
    #zip would be (1,4)(2,5)(3,6) i.e. combining the first element of both the arrays
    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

#second solution
import collections
def finder2(arr1,arr2):
    #collections are just used to add a default dict without adding any key
    #so if u didn't defined any key in the dict because of collections it won't show error
    d=collections.defaultdict(int)
    for num in arr2:
        #for every element in array2 add 1
        d[num]+=1
    for num in arr1:
        if d[num]==0:
            return num
        else:
            d[num]-=1


#another approach is to add all the elements of the arrays individually
#subtracting the sum from arr2 to arr1
#the difference would be the missing number
#but drawbacks in long array, decimal number array