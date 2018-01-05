''' write a function to to check and make unique pair of numbers in such a way hat they are equal to the sum
For example:-
pair_sum([1,3,2,2],4)
should return:-
[1,3]
[2,2]
pairs that are equal to sum i.e "4"
'''

def pair_sum(arr,k):
    #if the length is less than 2 , can not make a pair return
    if len(arr)<2:
        return
    #else
    seen=set()
    output=set()
    #for the numbers in array
    for num in arr:# going for first loop num=1
        target=k-num #target=4-1 i.e 3
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target)),max(num,target))
    return len(output)
    print '\n'.join(map(str,list(output)))