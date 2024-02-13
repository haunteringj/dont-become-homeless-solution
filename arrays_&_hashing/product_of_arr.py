class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []

        # prefix
        for i in range(len(nums)):
            answer.append(1)
            for j in range(0, i):
                answer[i] = answer[i] * nums[j]

        # postfix
        for i in range(len(nums), -1, -1):
            for j in range(len(nums) - 1, i, -1):
                answer[i] = answer[i] * nums[j]
                
        return answer
