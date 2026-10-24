class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Binary search hamesha chhoti array par karenge
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            # nums1 ka partition
            partition1 = (left + right) // 2

            # nums2 ka partition
            partition2 = (m + n + 1) // 2 - partition1

            # nums1 ke left side ka maximum
            if partition1 == 0:
                maxLeft1 = float('-inf')
            else:
                maxLeft1 = nums1[partition1 - 1]

            # nums1 ke right side ka minimum
            if partition1 == m:
                minRight1 = float('inf')
            else:
                minRight1 = nums1[partition1]

            # nums2 ke left side ka maximum
            if partition2 == 0:
                maxLeft2 = float('-inf')
            else:
                maxLeft2 = nums2[partition2 - 1]

            # nums2 ke right side ka minimum
            if partition2 == n:
                minRight2 = float('inf')
            else:
                minRight2 = nums2[partition2]

            # Correct partition mil gaya
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Odd total elements
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)

                # Even total elements
                return (
                    max(maxLeft1, maxLeft2)
                    + min(minRight1, minRight2)
                ) / 2.0

            # nums1 ka partition bahut right hai
            elif maxLeft1 > minRight2:
                right = partition1 - 1

            # nums1 ka partition left hai
            else:
                left = partition1 + 1