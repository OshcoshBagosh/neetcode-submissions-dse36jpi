class Solution:

    """
    For encode we will create a string in this format:
    "4#word2#to4#word"
    the numbers represent the length of the string and the
    "#" acts as delimiter for the end of number code 
    """

    def encode(self, strs: List[str]) -> str:
        #If strs is an empty list use special code
        if(len(strs) == 0):
            return "empty#"
        pack = ""
        for s in strs:
            pack += f"{len(s)}#{s}"
        return pack
    
    """
    For decode, we go through the encoded string and decode it based on 
    the lengths of each packed string.
    """
    def decode(self, s: str) -> List[str]:
        if s == "empty#":
            return []
        print(s)
        i = 0
        index = 0
        result = []
        while(i < len(s)):
            num = ""
            while(s[i] != "#"):
                num += s[i]
                i += 1
            i += 1
            length = int(num)
            result.append(s[i: i+length])
            index += 1
            i += length
        return result
