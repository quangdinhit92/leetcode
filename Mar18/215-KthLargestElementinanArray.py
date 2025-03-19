# def heapify(arr, i):
#     n = len(arr)
#     smallestIndex = i
#     smallest = arr[smallestIndex]
#     # check left is smallest
#     left = 2 * smallestIndex + 1
#     if left < n and arr[left] < smallest:
#         smallestIndex = left
#         smallest = arr[smallestIndex]

#     right = 2 * smallestIndex + 2
#     if right < n and arr[right] < smallest:
#         smallestIndex = right
#         smallest = arr[smallestIndex]

#     if smallestIndex != i:
#         arr[smallestIndex], arr[i] = arr[i], arr[smallestIndex]
#         heapify(arr, smallestIndex)

#     # check right is smallest


# def heapifyArr(arr):
#     for i in range(len(arr) // 2 - 1, -1, -1):
#         heapify(arr, i)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        ret = nums[0]
        for _ in range(k):
            ret = heapq.heappop(nums)
        return -ret
