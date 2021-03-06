# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

class Solution:
    # the function takes in a list of numbers as a parameter, and a target to check if the combination is possible
    # brute force method
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the length of numbers once
        for i in range(len(nums)):
          # iterate through the length of numbers again
            for j in range(len(nums)):
              # in the iteration if a combination is possible and the combination is not the same number twice
              # return the set of numbers that is possible
                if (nums[i] + nums[j] == target) and (i != j):
                    return([i, j])
                  
# ----------------------------------------- Problem 2 Easy - Palindrome ----------------------------------------------- #

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # reverse the string and then compare if the original string is the same
        return str(x) == str(x)[::-1]
      
# ----------------------------------------- Problem 3 Easy - Roman to Integer ----------------------------------------------- #



# ----------------------------------------- Problem 4 Easy - Running Sum of 1d Array ----------------------------------------------- #

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # nums' ith element is the sum of all elements till i-1
        for i in range(1, len(nums)):
            # since len(nums) - the second param is up to and not including
            nums[i] += nums[i - 1]
            print(i)
            # [1, 2, 3, 4] -> [1, 3, 6, 10]
        return nums
        

# ----------------------------------------- Problem 5 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 6 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 7 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 8 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 9 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 10 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 11 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 12 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 13 Easy - Two Sum ----------------------------------------------- #



# ----------------------------------------- Problem 14 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 15 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 16 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

# ----------------------------------------- Problem 1 Easy - Two Sum ----------------------------------------------- #

