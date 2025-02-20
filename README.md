# Unique Binary String Finder

## Overview
This repository contains a Python solution to find a unique binary string that is not present in a given list of binary strings. The approach ensures an efficient and simple way to generate the missing binary string.

## Problem Statement
Given a list of binary strings, each of length `n`, the task is to find a binary string of the same length that is not present in the given list.

## Implementation
The solution iterates through possible binary numbers, converts them to strings, and checks if they are in the input list. The first missing string is returned.

## Code
```python
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for i in range(n+1):
            st = f'{i:b}'.zfill(n)  # Convert to binary and pad with leading zeros
            if st not in nums:  # Check if it's missing in the list
                return st  # Return the first missing binary string
