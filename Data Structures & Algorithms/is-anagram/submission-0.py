class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s,dict_t={},{}
        for ele in s:
            if ele not in dict_s:
                dict_s[ele]=0
            dict_s[ele]+=1
        for ele in t:
            if ele not in dict_t:
                dict_t[ele]=0
            dict_t[ele]+=1
        for ele in s:
            if ele not in dict_t or dict_s[ele]!=dict_t[ele]:
                return False
        return True