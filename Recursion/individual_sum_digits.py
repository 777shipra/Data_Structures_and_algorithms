# write a function that would return the sum of all the individual digits of a number provided


def func_sum(n):

    if len(str(n))==1:
        return n
    else:
        return n%10+func_sum(n/10)


#let n =4253 , n%10 will give u 3 and n/10 will give u 425