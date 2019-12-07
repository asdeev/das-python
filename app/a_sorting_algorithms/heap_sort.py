from typing import List


def heapify(nums, heap_size, root_index):
    # assume the index of the largest element is at the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[largest], nums[root_index] = nums[root_index], nums[largest]
        # heapify the new root to ensure it is the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums: List[int]) -> List[int]:
    """This function will do a heap sort on the passed in array.

    This algorithm is similar to selection sort, which segments the array into sorted and unsorted parts.

    It will iterate over the unsorted segment and insert the element being viewed into the correct
        spot of the sorted list.

    Runs in O(nlog(n)) time: First n time to traverse array to create heap and then log(n) time to sort it

    :param nums: The unsorted integer array.
    :return: nums: The sorted integer array.

    """
    n = len(nums)

    # create the Max Heap from list
    # 2nd argument of range means it stops at the element before -1
    # 3rd argument of range means it iterates backwards, reducing the count of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # move root of the max heap to the end of the list
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums


def main():
    values = [0, 4, 100, 5000, 500, 30]

    values_sorted = heap_sort(nums=values)
    print(values_sorted)


if __name__ == '__main__':
    main()
