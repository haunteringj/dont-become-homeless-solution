class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (sorted(s) in sorted(t)) or (sorted(s) in sorted(t) or sorted(s) == sorted(t)):
            return True
        else:
            return False
    

    '''
    O(s+t) solution, 1 loop to sort s and t. (Using 'in' means a faster sol. No need to sort t potentially.)

    even eaiser, just do return sorted(t) == sorted(s) since it returns True/False anyways 

    '''

    '''
    Solution using HashMaps
    O(s+t) time complexity. Requires sorting both t and s.
    Uses get() on hashmap in the event the key does not exist i.e.
    {a,2; b, 1; null, null} -> here get(s[i], 0) will default set the value to 0.

    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
    print(count_s, count_t)
    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False

    return True



    Alternatively, you can just do. Counter does the same thing as above.

    if Counter(s) == Counter(t):
        return True
    else:
        return False
    '''