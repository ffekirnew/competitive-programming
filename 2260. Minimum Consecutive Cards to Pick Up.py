class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # brute force
        # answer = float('inf')
        # for i in range(len(cards)):
        #     for j in range(i + 1, len(cards)):
        #         if cards[i] == cards[j]:
        #             answer = min(answer, j - i + 1)
        #             break
        # return answer if (answer != float('inf')) else -1
        
        # create the object to be returned
        answer = float('inf')
        # create a hashmap to keep track of frequencies and first appearances
        freq = {}
        # loop through cards
        for i in range(len(cards)):
            card = cards[i]
            if card in freq:
                answer = min(answer, i - freq[card] + 1)
            freq[card] = i
        # return the anser
        return -1 if (answer == float('inf')) else answer
