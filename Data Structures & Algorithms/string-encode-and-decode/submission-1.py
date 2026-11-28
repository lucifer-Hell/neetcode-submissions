class Solution:

    def encode(self, strs: List[str]) -> str:
        splitter=chr(257)
        if not strs:
            return splitter
        print(splitter)
        print('joined str ',splitter.join(strs))
        return splitter.join(strs)


    def decode(self, s: str) -> List[str]:
        splitter=chr(257)
        if s==splitter:
            return []
        return s.split(splitter)
        
