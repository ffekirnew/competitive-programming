class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        # sort the citations       
        citations.sort()
        # loop through it and find the index with occurences greater or equal to its value, if the element at the index is less then it, return h_index
        n = len(citations)
        for i in range(0, n):
            if citations[n - 1 - i] > i:
                h_index += 1
            else:
                break
        # return the h_index
        return h_index
