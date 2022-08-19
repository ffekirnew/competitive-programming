class Solution:
    def sortSentence(self, s: str) -> str:
        unsorted_list = s.split(" ")
        index_list = [index for index in range(1, len(unsorted_list)+1)]

        sorted_string = [k.replace(str(j), '') for j in index_list
                                               for k in unsorted_list
                                               if str(j) in k]

        return ' '.join(sorted_string)