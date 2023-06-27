# 1. Two Sum

[Link](https://leetcode.com/problems/two-sum/description/)

**Easy**

## Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
### Examples


#### Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

#### Example 2:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

#### Example 3:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints

* 2 <= nums.length <= 10<sup>4</sup>

* -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>

* -10<sup>9</sup> <= target <= 10<sup>9</sup>

* Only one valid answer exists.


## Solutions

### Solution 1

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, v1 in enumerate(nums[:-1]):
            for i2, v2 in enumerate(nums[i1+1:]):
                if v1 + v2 == target:
                    return [i1, i2+i1+1]
```

Runtime 3367 ms   
Beats 33.17%

Memory 17 MB   
Beats 87.12%