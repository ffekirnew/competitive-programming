from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        # create the empty object to be returned
        original = []
        # count the frequencies of the items in the changed list
        freqDict = Counter(changed)
        # until the empty object solution is half the size of the doubled, check for each item in the frequency dictionary if the double exists and has the same frequency and add it to the original (with its frequency)
        for i in sorted(freqDict.keys()):
            # object size check before every looping
            if len(original) >= len(changed) // 2:
                break
            # if the item is zero, the double is also zero, so it needs to be considered on its own
            if i == 0:
                if freqDict[i] % 2 == 0:
                    original += [0] * (freqDict[i] // 2)
            elif 2 * i in freqDict:
                if freqDict[2 * i] >= freqDict[i]:
                    original += ([i] * freqDict[i])
                    freqDict[2 * i] -= freqDict[i]
        # return the solution
        return original if len(original) == len(changed) // 2 else []
