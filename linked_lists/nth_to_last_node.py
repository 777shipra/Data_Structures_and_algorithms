def nth_to_last_node(n,head):

    left_pointer=head
    right_pointer=head

    for i in xrange(n-1):

        if not right_pointer.nextnode:
            raise LookupError('Error: n is greater than the number of nodes')

        right_pointer=right_pointer.nextnode

    while right_pointer.nextnode:

        left_pointer=left_pointer.nextnode
        right_pointer=right_pointer.nextnode

    return left_pointer