from typing import List
from math import floor

def binary_search(arr: List[int], target: int) -> int:

    left, right =  0, len(arr)-1
    
    while left <=right:
        mid = (left+right)//2 # middle point
        if arr[mid] == target:
            return mid # found
        elif arr[mid] < target:
            left = mid+1  # discard left part of array
        else:
            rigth = mid-1 # discard right part of array
    return -1 
