class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #output is a 2D array
        """
        My idea is to implement my answer from isAnagram and
        compare each str with one another in the list of str
        """
        groupTable = {}

        for s in strs:
            placed = False
            for key in groupTable:
                if self.isAnagram(groupTable[key][0], s):
                    groupTable[key].append(s)
                    placed = True
                    break
            if not placed:
                    groupTable[len(groupTable)] = [s]

        return list(groupTable.values())
        
        return groupTable
        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmapS, hmapT = {}, {}

        for i in range(len(s)):
            hmapS[s[i]] = 0
            hmapT[t[i]] = 0
        
        for i in range(len(s)):
            hmapS[s[i]] += 1
            hmapT[t[i]] += 1

        return hmapS == hmapT