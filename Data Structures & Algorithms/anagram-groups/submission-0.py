from collections import defaultdict
class Solution:
    def isAnagram(self,i,j,strs)-> bool:
        word_a=strs[i]
        word_b=strs[j]
        dict_word=defaultdict(int)
        for char in word_a:
            dict_word[char]+=1
        for char in word_b:
            if char not in dict_word:
                return False
            if dict_word[char]==0:
                return False
            dict_word[char]-=1
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_a,visited = {},set()
        for i in range(len(strs)):
            if i in visited:
                continue
            dict_a[i]=[i]
            visited.add(i)
            for j in range(i+1,len(strs)):
                if self.isAnagram(i,j,strs):
                    dict_a[i].append(j)
                    visited.add(j)

        group_list=[]
        for values in dict_a.values():
            str_vals=[ strs[idx] for idx in values ]
            group_list.append(str_vals)
        return group_list
            

