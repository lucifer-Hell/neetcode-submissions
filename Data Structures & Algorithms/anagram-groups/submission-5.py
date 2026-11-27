from collections import defaultdict
class Solution:
    def getSign(self,value:str)->Tuple[int,...]:
        sig_arr=[0 for _ in range(26)]
        for char in value:                
            sig_arr[ord(char)-ord('a')]+=1
        return tuple(sig_arr)
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ana=defaultdict(list)
        for value in strs:
            value_sign=self.getSign(value)
            dict_ana[value_sign].append(value)
        # print('dictionary ',dict_ana)
        return [values for values in dict_ana.values()]
        
        