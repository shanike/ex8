

def constraint_satisfactions(n, blocks):
    """returns all possible filling for line of <n> int s according to <blocks> contraint
        (list of lists)

    Args:
        n (int): length of row
        blocks (int list): constraints
    """
    if sum(blocks) + len(blocks) - 1 < n:  # no possible fill
        return []

    final = []
    constraint_satisfactions_helper2(n, blocks, [], final)
    print("final: ")
    [print(x) for x in final]


def constraint_satisfactions_helper(n, blocks, arr, temp_arr=[], blocks_i=0):

    # if len(temp_arr) >= n:
    #     arr.append(temp_arr)
    #     print('arr: ', arr)
    #     return
    print("wwwwwwwwwwwww", arr, temp_arr, blocks_i)

    if blocks_i >= len(blocks):
        print('temp_arr: ', temp_arr)
        arr.append(temp_arr[:])
        print('arr: ', arr)
        return

    if len(temp_arr) + blocks[blocks_i] + 1 >= n:
        return True

# todo if that check if we came to the end of n length temp arr
    for i in range(blocks_i, len(blocks)):
        block = blocks[i]
        # temp_arr1 = temp_arr
        temp_arr.extend([1 for x in range(block)])
        for j in range(len(temp_arr) - 1, n):
            print("heloooo", j)
            temp_arr.append(0)
            if constraint_satisfactions_helper(n, blocks, arr, temp_arr, blocks_i=i + 1):
                print("byeeee")
                break
        # del temp_arr[-1*(block+1):len(temp_arr)]
        for g in range(j-1):
            temp_arr.pop()
            # temp_arr.append()
        # temp_arr.extend([1 for x in range(block)]+[0][0])


UNDECIDED = -1

    if blocks_i > len(blocks)+1 or len(temp_arr) == n:
        arr.append(temp_arr)
        return

def intersection_row(rows):
    """returns intersection of all rows. if no concrete intersection for pos i - will set pos i to -1

        :param rows: {list of list of numbers (1 0 or -1)}

    Returns:
        intersections -- list of numbers representing the intersection of columns in <rows>
    """
    # expecting = 0 (.e.g)
    # if == -1
        # לא אכפת
    # if == 1
        # not good
    merged_row = []
    for col in range(len(rows[0])):
        expecting = rows[0][col]
        broke_expectation = False
        for row in range(1, len(rows)):  # check the 1,
            print(f"value {rows[row][col]}")
            if rows[row][col] != expecting and rows[row][col] != -1:
                broke_expectation = True
        merged_row.append(UNDECIDED if broke_expectation else expecting)
    return merged_row


constraint_satisfactions(4, [1, 2])
