class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        count = []
        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1
            
            anagrams[tuple(count)].append(string)
    
        return anagrams.values()

        '''
        
        bascially, tea, eat, ate share the same letters. 1 a, 1 e, 1 t. 
        make a dict

        KEY             | VAL
        1 a, 1 e, 1 t   | [ate, eat, tea]
        use Ord(char) to get ASCII val and map it to dict
        then return lists of numbers
        '''



        '''
        res = []
        for i in range(len(strs)):
            anagrams = []
            for j in range(len(strs)):
                if (sorted(strs[i]) == sorted(strs[j]) and i != j):

                    anagrams.append(strs[j])
            anagrams.append(strs[i])
            res.append(sorted(anagrams))

        res = list(set(tuple(i) for i in res))
        res = [list(i) for i in res]

        return res
        Removes dupes from nested list
        res = [tuple(i) for i in res]

        # Now we can convert this to a set to remove duplicates
        res = list(set(res))
        '''

    

'''
time limit exceeded
O(m*log(n)) time complexity sol. 
where m is len of list
n is average length of the words
'''