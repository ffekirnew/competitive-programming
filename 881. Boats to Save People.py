class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # create the object to be returned
        answer = 0
        # sort the people
        people.sort()
        # use two pointers
        i, j = 0, len(people) - 1
        # loop through he people and match the heaviest and the lightest
        while i <= j:
            curr = people[i] + people[j] if i < j else people[i]
            if curr > limit:
                answer += 1
                j -= 1
            elif curr <= limit:
                answer += 1
                j -= 1
                i += 1
        # return the solution
        return answer
