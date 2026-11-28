class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for val in strs:
            encoded_str+=str(len(val))+'#'+val
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        print('encoded str ',s)
        # find the len 
        i=0
        while i<len(s):
            str_len=''
            str_val=''
            # print('curr i')
            # first set will always tell len
            while i<len(s) and s[i]!='#':
                str_len+=s[i]
                i+=1
            # skip start hash
            i+=1
            j=0
            while j<int(str_len):
                str_val+=s[i]
                i+=1
                j+=1
            decoded_strs.append(str_val)
        return decoded_strs 
            


