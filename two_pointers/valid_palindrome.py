class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for i in s:
            if i.isalnum():
                new_str += i
        
        new_str = new_str.lower()

        for i in range(len(new_str)):
            if new_str[i] != new_str[len(new_str) - i - 1]:
                return False

        return True
        

    '''
    O(n) time complexity. Check if all values are alpha.numeric, then use 2 pointers from front ant back to check for matching values
    '''