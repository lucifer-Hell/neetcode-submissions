from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base condn for strings to must be in anagaram
        if len(s)!=len(t):
            return False
        freq=defaultdict(int)
        for ele in s:
            freq[ele]+=1
        print('freq s ',freq)
        for ele in t:
            if ele not in freq:
                return False
            freq[ele]-=1
        print('freq t ',freq)
        return all(ele for ele in freq.values())==0
        

        