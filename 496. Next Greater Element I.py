class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        new_dictionary = {}
        new_list = []

        for index in range(len(nums2)):
            if nums2[index] in nums1:
                number = nums2[index]
                rest = nums2[index+1:]
                new_dictionary[number] = rest

        for num in nums1:
            if new_dictionary[num] == []:
                new_list.append(-1)
            else:
                index2 = 0
                while len(new_dictionary[num]) > 0:
                    i = new_dictionary[num][index2]
                    if i > num:
                        new_list.append(i)
                        break
                    else:
                        index += 1
                        new_dictionary[num].remove(i)
                if new_dictionary[num] == []:
                    new_list.append(-1) 

        return new_list