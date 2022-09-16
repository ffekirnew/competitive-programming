class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # an object to keep track of which charachters are already in the current substring
		chars = {}
        # an object to be returned
		longest = 0
        # a temporary variable that might change the longest
		current = 0
        # the starting index of the current substring
		start = 0
        for i in range(len(s)):
            current_char = s[i]
            # if the charachter is already registered
			if current_char in chars:
                # if the previous location is before the start of the current substring, it means nothing and we continue
				if chars[current_char] < start: current += 1
                # if not, tho, the start needs to be moved to that location, and the current length reduced to the difference between the current location of the charachter and the previous one
				else: current, start = i - chars[current_char], chars[current_char] + 1
            # if the charachter is a new one
			else: current += 1
            # regardless of what happened the current location of the charachter must be changed
			chars[current_char] = i
            
            if current > longest: longest = current
        
        return longest
