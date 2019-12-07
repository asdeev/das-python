from typing import List


def search(self, nums: List[int], target: int) -> int:
    first = 0
    last = len(nums) - 1
    found = -1

    while first <= last and found == -1:
        mid = (first + last) // 2

        if nums[mid] == target:
            found = mid
        elif target < nums[mid]:
            last = mid - 1
        elif target > nums[mid]:
            first = mid + 1
    return found

