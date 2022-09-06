class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {} # a dictionary to hold the characters in the string, going to store them in the format {'char' : [multiplicity, first_appearance_index]}
        for i in range(len(s)):
            char = s[i]
            if char in chars.keys(): # if the charachter already exists in the map, just increase its multiplictity
                chars[char][0] += 1
            else: # else add it to the map with multiplicity 1 and the current index
                chars[char] = [1, i]
        
        indexes = list(chars.values()) # now the indexs are the values of the map
        indexes.sort() # sort it (multiplicities will be used to sort it)
        if indexes[0][0] > 1: # if the smallest multiplicity is greater that one, then there is not unique char, return -1
            return -1
        else: # else return the first index
            return indexes[0][1]