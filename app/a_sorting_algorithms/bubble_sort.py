from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """This function will do a bubble sort on the passed in array.

    It compares elements in pairs and swaps them until the larger elements "bubble up" to the
        end of the list.

    Runs in O(n^2) for worst case with n elements: When array is in reverse order
    Runs in O(n) for best case with n elements: When array is already sorted

    :param nums: The unsorted integer array.
    :return: nums: The sorted integer array.

    """
    # create flag to let algorithm know when sorting is finished
    # without this flag, it will always run in O(n^2) time even while pre-sorted
    do_sort = True

    while do_sort:
        do_sort = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                do_sort = True
    return nums


def main():
    values = [0, 4, 100, 5000, 500, 30]

    values_sorted = bubble_sort(nums=values)
    print(values_sorted)


if __name__ == '__main__':
    main()
