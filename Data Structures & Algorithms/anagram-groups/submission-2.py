from collections import defaultdict
class Solution:
    def getSign(self,value:str)->str:
        sig_arr=[0 for _ in range(26)]
        for char in value:
            sig_arr[ord(char)-97]+=1
        sig_str=''
        for ele in sig_arr:
            sig_str+=str(ele)
        return sig_str
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ana=defaultdict(list)
        for value in strs:
            value_sign=self.getSign(value)
            dict_ana[value_sign].append(value)

        return [values for values in dict_ana.values()]
        
        