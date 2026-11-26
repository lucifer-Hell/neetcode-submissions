from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base condn for strings to must be in anagaram
        if len(s)!=len(t):
            return False
        freq=defaultdict(int)
        for ele in s:
            freq[ele]+=1
        for ele in t:
            if freq[ele]==0:
                return False
            freq[ele]-=1
        return True        

        