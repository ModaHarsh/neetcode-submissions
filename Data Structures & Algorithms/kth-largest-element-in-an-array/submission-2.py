class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]        

        ## heapq.nlargest(k, heap)
        ## returns the n largest element in an array 
        ## in a decreasing order
        ## it forms a heap of length k internally 
        ## by iterating though all n elements and then returns the
        ## k largest elements

        ## overall TC is O( n logk )
        ## n elements to iterate for 
        ## and k elements to be stored in the array
