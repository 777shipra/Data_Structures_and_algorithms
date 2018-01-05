#For given array consisting all negative all positive or both find the largest continuour sum


def larg_cont_sum(arr):
    if len(arr)==0:
        return None
    max_sum=current_sum=arr[0]

    for num in arr[1:]:
        current_sum=max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)

    return max_sum


