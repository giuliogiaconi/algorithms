import statistics, math


def quick_sort(number_list, pivot_type):
    """Returns the number of comparisons performed by the quick sort algorithm when sorting the number_list.

    Args:
        number_list (list): list of numbers to sort
        pivot_type (string): select the strategy for choosing the pivot. If "first" the pivot is always chosen as the first element of the array. If "last", the pivot is the last element of the array

    Returns:
        int: sum of comparisons performed by the algorithm
    """

    # base case
    if len(number_list) <= 1:

        # print('base case: ', number_list)

        return 0

    # recursion step
    else:

        smaller = []
        larger = []

        # print('recursion step: ', number_list)

        if pivot_type == "first":

            pivot = number_list[0]

        elif pivot_type == "last":

            pivot = number_list[-1]
            number_list[-1], number_list[0] = number_list[0], number_list[-1]

        # print(number_list)
        i = 1

        for j in range(1, len(number_list)):

            # swap elements
            if number_list[j] <= pivot:

                number_list[i], number_list[j] = number_list[j], number_list[i]
                i += 1

        number_list[0], number_list[i - 1] = number_list[i - 1], number_list[0]
        # print('after partition', number_list)
        # print('pivot index', i-1)
        sum_comparisons_current = len(number_list) - 1
        sum_comparisons_smaller = quick_sort(number_list[0 : i - 1], pivot_type)
        sum_comparisons_larger = quick_sort(number_list[i:], pivot_type)
        # print('smaller: ', number_list[0:i-1], sum_comparisons_smaller, number_list)
        # print('larger: ', number_list[i:], sum_comparisons_larger, number_list)
        # print(sum_comparisons_current, sum_comparisons_smaller, sum_comparisons_larger)
        return (
            sum_comparisons_current + sum_comparisons_smaller + sum_comparisons_larger
        )


def quick_sort_median(number_list):
    """Returns the number of comparisons performed by the quick sort algorithm when sorting the number_list. The pivot is chosen as the median element in the array.

    Args:
        number_list (list): list of numbers to sort

    Returns:
        int: sum of comparisons performed by the algorithm
    """

    # base case
    if len(number_list) <= 3:

        # print('base case: ', number_list)

        return max(len(number_list) - 1, 0)

    # recursion step
    else:

        # print('recursion step: ', number_list)

        pivot_1 = number_list[0]
        pivot_2 = number_list[-1]
        if len(number_list) % 2 == 0:
            pivot_3_index = int((len(number_list) / 2) - 1)
            pivot_3 = number_list[pivot_3_index]
        else:
            pivot_3_index = math.ceil(len(number_list) / 2) - 1
            pivot_3 = number_list[math.ceil(len(number_list) / 2) - 1]

        my_dict = {pivot_1: 0, pivot_2: len(number_list) - 1, pivot_3: pivot_3_index}
        # print(pivot_1, pivot_2, pivot_3)
        # print(my_dict)
        pivot = statistics.median([pivot_1, pivot_2, pivot_3])
        pivot_index = my_dict[pivot]

        # print(pivot, pivot_index)
        number_list[0], number_list[pivot_index] = (
            number_list[pivot_index],
            number_list[0],
        )
        # print(number_list)

        i = 1
        for j in range(1, len(number_list)):

            # swap elements
            if number_list[j] <= pivot:

                number_list[i], number_list[j] = number_list[j], number_list[i]
                i += 1

        number_list[0], number_list[i - 1] = number_list[i - 1], number_list[0]

        sum_comparisons_current = len(number_list) - 1
        sum_comparisons_smaller = quick_sort_median(number_list[0 : i - 1])
        sum_comparisons_larger = quick_sort_median(number_list[i:])
        # print('smaller: ', smaller)
        # print('larger: ', larger)
        # print(sum_comparisons_current, sum_comparisons_smaller, sum_comparisons_larger)
        return (
            sum_comparisons_current + sum_comparisons_smaller + sum_comparisons_larger
        )



# lines = [4,7,5,3,1,10,8]
# lines = [1, 5, 4, 8, 7, 6, 10, 21, 15, 3]
number_inversion = quick_sort(lines, "first")
print(number_inversion)
print("======")

# lines = [4,7,5,3,1,10,8]
number_inversion = quick_sort(lines, "last")
print(number_inversion)
print("======")

# lines = [4,7,5,3,1,10,8]
number_inversion = quick_sort_median(lines)
print(number_inversion)
