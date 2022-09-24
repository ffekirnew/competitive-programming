#User function Template for python3

class Solution:
    def selectionSort(self, arr,n):
        i = 0
        while i < len(arr) - 1:
            minimum = i
            j = i + 1
            while j < len(arr):
                if arr[minimum] > arr[j]:
                    minimum = j
                j += 1
            arr[i], arr[minimum] = arr[minimum], arr[i]
            i += 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
