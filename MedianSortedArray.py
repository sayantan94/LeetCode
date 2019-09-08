class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        return ( self.median(nums1,len(nums1))  )
        
    def median(self,arr,n):
        if not arr:
            return float(0)
        if n%2 == 0:
            return float( (arr[int(n/2)] + arr[int(n/2)-1]) / 2)
        else:
            return float(arr[int(n/2)] )
        
        
        
if __name__ == '__main__':
    # The arrays are already sorted
    nums1 = []
    nums2 = [2]
    print (Solution().findMedianSortedArrays(nums1, nums2))
    
    