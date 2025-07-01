class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            stringLength = str(len(string))
            delimiter = '#'
            encodedString += delimiter + stringLength + delimiter + string

        return encodedString


    def decode(self, s: str) -> List[str]:
        decodedList = []
        index = 0
        delimiter = '#'
        #   "#4#This#2#is#2#an#7#example"
        while (index < len(s)):
    
            if (s[index] == delimiter): 
                index += 1 #skip past first delimiter
                
                delimiter_index = s.find('#', index) #find the NEXT '#'
                length = int(s[index: delimiter_index]) # converts the string between #'s to a number
                index = delimiter_index + 1 # take one past 2nd '#' AKA beginning of word

                word = ""
                word = s[index:index + length] #word is grabbed by the delimiter data (this prevents confusion by #'s included in string itself)

                decodedList.append(word)
                index += length 
            else:
                index +=1
        return decodedList
