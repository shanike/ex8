

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
    res = constraint_satisfactions_helper(n, blocks, final)
    print("final final: ", final)


def constraint_satisfactions_helper(n, blocks, arr, temp_arr=[], blocks_i=0):

    # if len(temp_arr) >= n:
    #     arr.append(temp_arr)
    #     print('arr: ', arr)
    #     return
    print("wwwwwwwwwwwww", arr, temp_arr, blocks_i)

    if blocks_i >= len(blocks) - 1:
        print('arr: ', arr)
        print('temp_arr: ', temp_arr);
        arr.append(temp_arr)
        print('arr: ', arr)
        return True

    if len(temp_arr) + blocks[blocks_i] + 1 < n:
# todo if that check if we came to the end of n length temp arr
        for i in range(blocks_i, len(blocks)):
            block = blocks[i]
            temp_arr1 = temp_arr
            temp_arr.extend([1 for x in range(block)])
            for j in range(len(temp_arr) - 1, n):
                temp_arr.append(0)
                if not constraint_satisfactions_helper(n, blocks, arr, temp_arr, blocks_i=i + 1):
                    break
            # del temp_arr[-1*(block+1):len(temp_arr)]
            temp_arr = temp_arr1
                # temp_arr.append()
            # temp_arr.extend([1 for x in range(block)]+[0][0])

def constraint_satisfactions_helper3(n, blocks, single_fill, fill_pos, finals):

    if fill_pos >= n-1:
        return False

    else:

        # single_fill.append(0)
        # single_fill = [0] * fill_pos

        for i in range(len(blocks)):

            constraint = blocks[i]

            if fill_pos + constraint >= n:  # not good --> x
                return False

            single_fill.extend([1 for x in range(constraint)])

            res = constraint_satisfactions_helper(
                n, blocks[i:], single_fill, fill_pos+1, finals)

            # single_fill.append(0)  # for next #?


def constraint_satisfactions_helper2(n, blocks, single_fill, fill_pos, finals):
    """returns all possible filling for line of <n> int s according to <blocks> contraint
        (list of lists)

    Args:
        n (int): length of row
        blocks (int list): constraints
    """
    if fill_pos >= n - 1:
        print('single_fill: ', single_fill)
        finals.append(single_fill)
        return single_fill  # ?

    # for i in range(start, 3):
    # constraint_satisfactions(n, blocks, i=i+1)
    for i in range(len(blocks)):
        constraint = blocks[i]
        print('constraint: ', constraint)
        # for n_i in range(fill_pos, n):  # ?
        if can_fill_sqrs(constraint, n, single_fill):
            # fill single_fill with 1s, as many as the number in blocks[i] is
            single_fill.extend([1 for x in range(constraint)] + [0])
            print('single_fill: ', single_fill)
    constraint_satisfactions_helper(n,
                                    blocks,
                                    # i+constraint+1 --> is the next index in <fill> we can try to fill
                                    single_fill=single_fill,
                                    fill_pos=fill_pos+constraint+1,
                                    finals=finals
                                    )
    # finals.pop()  # ?
    # fills[start][len(fills[start]) - 1] = 0


def can_fill_sqrs(blocks, n, fill):
    return True


constraint_satisfactions(4, [1, 2])


def constraint_satisfactions_helper1(n, blocks, start, fills):
    """returns all possible filling for line of <n> int s according to <blocks> contraint
        (list of lists)

    Args:
        n (int): length of row
        blocks (int list): constraints
    """

    if not can_fill_sqrs(blocks, n, fills):
        return False

    # for i in range(start, 3):
    constraint_satisfactions(n, blocks, start+1)
    for i, constraint_int in enumerate(blocks):
        fills[i].append(1)
        constraint_satisfactions(n, blocks, start+1)
        fills[start][len(fills[start]) - 1] = 0

    # n==3 blocks==[1]
    #
    # [0, 0, 0]
    #
