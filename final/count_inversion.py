from copy import copy


# Brute Force, O(n^2)
def count_inversion_BF(num):
    count = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] > num[j]:
                count += 1
    return count


# Divide and Conque, O(nlogn)
def count_inversion_DnC(num):
    return inversion_helper(num,  0, len(num) - 1)


def inversion_helper(num, left_index, right_index):
    if left_index == right_index:
        return 0

    middle_index = int((left_index + right_index) / 2)

    inversions = inversion_helper(num,  left_index, middle_index)
    inversions += inversion_helper(num,  middle_index + 1, right_index)
    return inversions + inversion_merge_helper(num, left_index, middle_index, right_index)


def inversion_merge_helper(num, small_index, middle_index, high_index):
    second_num = copy(num)
    inversions = 0
    i = second_num_index = small_index
    j = middle_index + 1

    while True:
        if i > middle_index or j > high_index:
            break

        if num[i] > num[j]:
            # Inversion
            inversions += (middle_index + 1 - i)
            second_num[second_num_index] = num[j]
            j += 1
        else:
            # No inversion
            second_num[second_num_index] = num[i]
            i += 1
        second_num_index += 1

    for difference in range(middle_index - i + 1):
        second_num[second_num_index] = num[i + difference]
        second_num_index += 1

    for difference in range(high_index - j + 1):
        second_num[second_num_index] = num[j + difference]
        second_num_index += 1

    # Set this section of the original list equal to the sorted list
    # for index in range(small_index, high_index + 1):
    for index in range(small_index, high_index + 1):
        num[index] = second_num[index]

    return inversions


if __name__ == "__main__":
    num = [3, 6, 8, 9, 0, 1, 34, 56, 73, 23, 345, 65, 37, 25]

    print("Brute Force: ", count_inversion_BF(num))
    print("Divide and Conquer: ", count_inversion_DnC(num))
