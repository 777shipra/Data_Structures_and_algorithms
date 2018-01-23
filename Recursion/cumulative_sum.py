def cum_sum(n):

    if n==0:
        return 1
    else:
        return n + cum_sum(n-1)