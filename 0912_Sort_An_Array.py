""" Sort Algorithm """
from typing import List


# Bubble Sort
def bubbleSort(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(n - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# Selection Sort
def selectSort(nums):
    n = len(nums)
    for i in range(n):
        p = i
        for j in range(i, n):
            if nums[j] < nums[p]:
                p = j
        nums[i], nums[p] = nums[p], nums[i]
    return nums


# Insertion Sort
def insertSort(nums):
    n = len(nums)
    for i in range(1, n):
        temp, j = nums[i], i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
    return nums


# Quick Sort
def quickSort(nums, lo, hi):
    if lo < hi:
        pivot = partition(nums, lo, hi)
        quickSort(nums, lo, pivot - 1)
        quickSort(nums, pivot + 1, hi)
    return nums


def partition(nums, lo, hi):
    pivot = nums[lo]
    while lo < hi:
        while lo < hi and nums[hi] >= pivot:
            hi -= 1
        nums[lo] = nums[hi]
        while lo < hi and nums[lo] <= pivot:
            lo += 1
        nums[hi] = nums[lo]
    nums[lo] = pivot
    return lo


# Heap Sort
def heapSort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        adjust(nums, i, n)
    for j in range(n - 1, 0, -1):
        nums[0], nums[j] = nums[j], nums[0]
        adjust(nums, 0, j)
    return nums


def adjust(nums, i, n):
    temp = nums[i]
    while (k := i * 2 + 1) < n:
        if k + 1 < n and nums[k] < nums[k + 1]:
            k += 1
        if temp < nums[k]:
            nums[i] = nums[k]
            i = k
        else:
            break
    nums[i] = temp


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return quickSort(nums, 0, len(nums) - 1)


print(Solution().sortArray(nums=[19, 3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46]))
