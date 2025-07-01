class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        strs act



        '''
        encodedString = ""
        delimiter = "NeetCodeSolution" # length = 17
        for strings in strs:
            encodedString = encodedString + strings + delimiter
        return encodedString


    def decode(self, s: str) -> List[str]:
        delimiter = "NeetCodeSolution"
        if s == "":
            return []
        return s.split(delimiter)[:-1]  
        
        

