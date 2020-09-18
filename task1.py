import sys


def max_subarray(numbers):

    best_sum = 0
    best_start = best_end = 0
    current_sum = 0
    max_elem = -10e9999
    for current_end, x in enumerate(numbers):

        if x > max_elem:
            max_elem = x
            max_idx = current_end

        if current_sum <= 0:

            current_start = current_end
            current_sum = x
        else:

            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1

    if best_sum == 0:
        best_sum = max_elem
        return numbers[max_idx]

    return numbers[best_start:best_end]


if __name__ == '__main__':

    array = sys.argv[1]
    a_list = array.split()
    map_object = map(int, a_list)
    array = list(map_object)
    print('Array: ', array)
    print('Max subarray: ', max_subarray(array))
