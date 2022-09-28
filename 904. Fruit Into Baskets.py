class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # create the object to be returned
        maximum = 0
        # create a variables to hold which fruits are being picked currently
        f1 = None
        f2 = None
        f1_recent = None
        f2_recent = None
        # set up the sliding window
        start = 0
        end = 0
        # loop through the array
        while end < len(fruits):
            if f1 == fruits[end] or f1 == None:
                f1, f1_recent = fruits[end], end
            elif f2 == fruits[end] or f2 == None:
                f2, f2_recent = fruits[end], end
            else:
                if f1_recent > f2_recent:
                    start = f2_recent + 1
                else:
                    start = f1_recent + 1
                    f1, f1_recent = f2, f2_recent
                f2, f2_recent = fruits[end], end
            maximum = max(end - start + 1, maximum)
            end += 1
        # return the object
        return maximum
