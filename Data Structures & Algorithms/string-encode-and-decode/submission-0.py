class Solution:

    def encode(self, strs: List[str]) -> str:
        splitter=chr(257)
        print(splitter)
        return splitter.join(strs)


    def decode(self, s: str) -> List[str]:
        splitter=chr(257)
        return s.split(splitter)
