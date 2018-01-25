def permute(s):

    out=[]

    if len(s)==1:
        out=[s]

    else:

        for i,letter in enumerate(s):
            for perm in permute(s[:i]+s[1+1:]):

                out+=[letter+perm]

    return out

