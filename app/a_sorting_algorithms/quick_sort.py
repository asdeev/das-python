from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    """This function will do a quick sort

    This algorithm is similar to selection sort, which segments the array into sorted and unsorted parts.

    It will iterate over the unsorted segment and insert the element being viewed into the correct
        spot of the sorted list.

    Runs in O(n^2) for worst case with n elements: When array is in reverse order
    Runs in O(n) for best case with n elements: When array is already sorted

    :param nums: The unsorted integer array.
    :return: nums: The sorted integer array.

    """
    # start on the second value as the first value is assumed to be sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]

        j = i - 1

        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    return nums


def main():
    values = [0, 4, 100, 5000, 500, 30]

    values_sorted = insertion_sort(nums=values)
    print(values_sorted)


if __name__ == '__main__':
    main()
