class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        index = 1
        while index < len(intervals):
            pre_interval, interval = intervals[index - 1], intervals[index]
            pre_int_e = intervals[index - 1][1]
            int_s, int_e = intervals[index][0], intervals[index][1]
            
            if int_e < pre_int_e:
                intervals.pop(index)
                
            elif int_s <= pre_int_e:
                pre_interval[1] = interval[1]
                intervals.pop(index)
            
            else:
                index += 1
        
        return intervals