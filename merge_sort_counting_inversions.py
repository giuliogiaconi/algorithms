import random


def merge_sort(number_list):
    """Python implementation of the merge sort recursive algorithm

    Args:
        number_list (list): List of numbers to be sorted

    Returns:
        list: sorted list
    """

    # base case
    if len(number_list) <= 2:

        if len(number_list) == 1:
            return number_list
        else:
            number_list = [min(number_list), max(number_list)]
        return number_list

    else:

        # recursive step
        sorted_list_1 = merge_sort(number_list[0 : int(len(number_list) / 2)])
        sorted_list_2 = merge_sort(number_list[int(len(number_list) / 2) :])
        i = 0
        j = 0
        merged_list = []
        for k in range(len(sorted_list_1) + len(sorted_list_2)):
            if (
                i <= len(sorted_list_1) - 1
                and j <= len(sorted_list_2) - 1
                and sorted_list_1[i] <= sorted_list_2[j]
            ) or j > len(sorted_list_2) - 1:
                merged_list.append(sorted_list_1[i])
                i += 1
            elif (
                j <= len(sorted_list_2) - 1
                and i <= len(sorted_list_1) - 1
                and sorted_list_1[i] > sorted_list_2[j]
            ) or i > len(sorted_list_1) - 1:
                merged_list.append(sorted_list_2[j])
                j += 1

        return merged_list


def count_inversion(number_list):
    """Python implementation of the recursive algorithm used to count the number of inversions (e.g. out of order items) in a list of numbers. Based on the merge sort algorithm.

    Args:
        number_list (list): list of numbers

    Returns:
        list: sorted list of numbers
        int: number of inversions in the input list of numbers
    """

    if len(number_list) <= 2:

        # print('base case')
        # print('number_list', number_list)
        if len(number_list) == 1:
            return number_list, 0
        else:
            if min(number_list) != number_list[0]:
                number_inversion = 1
            else:
                number_inversion = 0
            number_list = [min(number_list), max(number_list)]

        return number_list, number_inversion

    else:

        # print('recursive step')
        sorted_list_1, number_inversion_1 = count_inversion(
            number_list[0 : int(len(number_list) / 2)]
        )
        sorted_list_2, number_inversion_2 = count_inversion(
            number_list[int(len(number_list) / 2) :]
        )
        # print('sorted_lists', sorted_list_1, sorted_list_2)
        # print('inversions', number_inversion_1, number_inversion_2)
        i = 0
        j = 0
        merged_list = []
        number_inversion_3 = 0
        for k in range(len(sorted_list_1) + len(sorted_list_2)):
            if (
                i <= len(sorted_list_1) - 1
                and j <= len(sorted_list_2) - 1
                and sorted_list_1[i] <= sorted_list_2[j]
            ) or j > len(sorted_list_2) - 1:
                merged_list.append(sorted_list_1[i])
                i += 1
            elif (
                j <= len(sorted_list_2) - 1
                and i <= len(sorted_list_1) - 1
                and sorted_list_1[i] > sorted_list_2[j]
            ) or i > len(sorted_list_1) - 1:
                merged_list.append(sorted_list_2[j])
                if i <= len(sorted_list_1) - 1:
                    number_inversion_3 += len(sorted_list_1) - i
                j += 1
        # print('res merging', merged_list, number_inversion_3)

        return merged_list, number_inversion_1 + number_inversion_2 + number_inversion_3


# number_list = random.sample(range(0, 10), 4)
# number_list = [5, 9, 6, 3, 1, 2, 0]
# print(number_list)
res, number_inversion = count_inversion(number_list)
print(number_inversion)
