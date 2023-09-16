# https://leetcode.com/problems/contains-duplicate/

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Hashmap solution
        Time complexity: O(n)
        Memory complexity: O(n)
        ''' 

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False


        '''
        Sorting solution

        Time complexity: O(nlog(n))
        Memory complexity: O(1)

        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
                
        return False

        ---------------------------------------------------

        Brute force solution
        
        Time complexity: O(n^2)
        Memory complexity: O(1)... No extra memory required

        for i in nums:
            count = 0
            for j in nums:
                if i == j:
                    count+= 1
            if count > 1:
                return True
        return False
        '''