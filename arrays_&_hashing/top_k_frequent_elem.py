class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elems = {}

        for i in nums:

            # count[n] = 1 + count.get(n, 0)
            if i not in elems:
                elems[i] = 0
            elems[i] += 1
        
        # sorted(tuple, lamdba to say the 2nd value)
        sorted_elems = sorted([(k, v) for k, v in elems.items()], key = lambda x: x[1], reverse=True)
        print(sorted_elems)

        res = []
        for i in range(0,k):
            res.append(sorted_elems[i][0])

        '''
        res = []
        for i in elems.keys():
            if elems[i] >= k:
                res.append(i)
        '''

        return res

'''
I did this one all by myself :) good job me

O(n*log(n))??? 

bascially, make a count of all the elements and put them into a dict
then reverse sort the dict (by turning it into a list of tuples)
add to the result until we reach the kth largest elem
return :)
'''
        