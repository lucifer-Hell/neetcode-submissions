class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f'{len(val)}#{val}' for val in strs])

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        idx=0
        while idx<len(s):
            str_len=''
            while idx<len(s) and s[idx]!='#':
                str_len+=s[idx]
                idx+=1
            decoded_strs.append(s[idx+1:idx+int(str_len)+1])
            idx=idx+int(str_len)+1
        return decoded_strs
