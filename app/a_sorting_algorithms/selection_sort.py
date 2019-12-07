from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    """This function will do a selection sort on the passed in array.

    This algorithm will segment the list into two parts: sorted and unsorted. It will continuously
        remove the smallest element of the unsorted segment of the list and append it to the sorted segment.

    Runs in O(n^2) time: O(n) for outer loop, O(n-1) + (n-2) + ... + 1 for inner loop -> O(n^2) overall

    :param nums: The unsorted integer array.
    :return: nums: The sorted integer array.

    """
    # the value of i represents how many values were sorted
    for i in range(len(nums)):
        # assume that the lowest index value is at i to start with
        lowest_index = i
        # inner loop iterates over the unsorted segment
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_index]:
                lowest_index = j
        # swap values of lowest unsorted element with the first unsorted element
        nums[i], nums[lowest_index] = nums[lowest_index], nums[i]
    return nums


def main():
    values = [0, 4, 100, 5000, 500, 30]

    values_sorted = selection_sort(nums=values)
    print(values_sorted)


if __name__ == '__main__':
    main()
