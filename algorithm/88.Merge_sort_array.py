class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1 = nums1 + nums2

        nums1 = [x for x in nums1 if x != 0]

        nums1.sort()

        return nums1
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    