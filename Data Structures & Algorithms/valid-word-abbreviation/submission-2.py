class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        index = 0
        i = 0
        while i < len(abbr):
            curr_num = 0
            if not abbr[i].isdigit():
                if index >= len(word) or abbr[i] != word[index]:
                    return False
                index += 1
                i += 1
            else:
                while i < len(abbr) and abbr[i].isdigit():
                    if curr_num == 0 and int(abbr[i]) == 0:
                        return False
                    curr_num = (curr_num * 10) + int(abbr[i])
                    i += 1
                print(curr_num)
                print(word[index:])
                print(len(word[index:]))
                if curr_num > len(word[index:]):
                    return False
                index += curr_num
                
        return True
        